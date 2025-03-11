#include "ConfigManager.h"
#include <stdexcept>

ConfigManager::ConfigManager(const std::string& configPath)
    : _configPath(configPath)
{
    loadConfig();
}

ConfigManager& ConfigManager::getInstance(const std::string& configPath)
{
    static ConfigManager instance(configPath);
    return instance;
}

void ConfigManager::loadConfig()
{
    try {
        _config = YAML::LoadFile(_configPath);
    } catch (const std::exception& e) {
        throw std::runtime_error(std::string("Error loading config: ") + e.what());
    }
}

std::string ConfigManager::get(const std::string& key, const std::string& defaultValue) const
{
    if (_config[key]) {
        return _config[key].as<std::string>();
    }
    return defaultValue;
}

YAML::Node ConfigManager::getSection(const std::string& section) const
{
    if (_config[section]) {
        return _config[section];
    }
    return YAML::Node();
}
