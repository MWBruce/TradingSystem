#include "MainTradingSystemBackend.h"
#include "../config_manager/ConfigManager.h"
#include <iostream>

void runBackend()
{
    ConfigManager& configManager = ConfigManager::getInstance();

    std::cout << "Success" << std::endl;
}
