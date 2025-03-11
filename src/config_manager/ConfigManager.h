#ifndef CONFIG_MANAGER_H
#define CONFIG_MANAGER_H

#include <string>
#include <yaml-cpp/yaml.h>

/**Singleton config manager**/
class ConfigManager {
public:

    static ConfigManager& getInstance(const std::string& configPath = "config/global_config.yaml");
    std::string get(const std::string& key, const std::string& defaultValue = "") const;
    YAML::Node getSection(const std::string& section) const;

private:
    explicit ConfigManager(const std::string& configPath);
    ~ConfigManager() = default;
    ConfigManager(const ConfigManager&) = delete;
    ConfigManager& operator=(const ConfigManager&) = delete;
    void loadConfig();

private:
    std::string _configPath;
    YAML::Node  _config;
};

#endif // CONFIG_MANAGER_H
