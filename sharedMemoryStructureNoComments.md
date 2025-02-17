my_trading_system/
├── config/
│   ├── global_config.yaml
│   ├── data_manager_configs/
│   │   ├── commodities.yaml
│   │   ├── currencies.yaml
│   │   └── equities.yaml
│   ├── strategies.yaml
│   └── investments.yaml
├──src/
│   ├── backend/
│   │   ├── trading_system/
│   │   │   ├── data_managers/
│   │   │   │   ├── base_data_manager.cpp
|   │   │   │   ├── base_data_manager.hpp
|   │   │   │   ├── ticker_manager.cpp
|   │   │   │   ├── ticker_manager.hpp
|   │   │   │   ├── orderbook_manager.cpp
|   │   │   │   └── orderbook_manager.hpp
|   │   │   ├── portfolio_manager/
|   │   │   │   ├── portfolio_manager.cpp
|   │   │   │   └── portfolio_manager.hpp
|   │   │   └── main_trading_system.cpp
|   │   ├── event_queue_manager/
|   │   │   ├── kafka_consumer.cpp
|   │   │   ├── kafka_producer.cpp
|   │   │   └── main_event_queue_manager.cpp
|   │   └── common_backend/
|   │       ├── logger.cpp
|   │       └── logger.hpp
|   ├── db_service/
|   │   ├── db_listener.cpp
|   │   ├── db_interface.cpp
|   │   ├── db_interface.hpp
|   │   ├── main_db_service.cpp
|   │   └── logger.cpp
|   ├── shared_memory/
|   │   ├── shared_memory_manager.cpp
|   │   ├── shared_memory_manager.hpp
|   │   ├── ring_buffer.cpp
|   │   └── ring_buffer.hpp
|   ├── event_pipeline_connection/
|   │   ├── event_pipeline_connection.cpp
|   │   └── event_pipeline_connection.hpp
|   ├── strategies/
|   │   ├── strategy_a/
|   │   │   ├── __init__.py
|   │   │   ├── live.cpp
|   │   │   ├── live.py
|   │   │   ├── config.yaml
|   │   │   ├── data_collector.cpp
|   │   │   ├── data_collector.hpp
|   │   │   ├── preprocessor.cpp
|   │   │   ├── preprocessor.hpp
|   │   │   ├── backtesting.cpp
|   │   │   ├── backtesting.hpp
|   │   │   ├── research.cpp
|   │   │   ├── research.hpp
|   │   │   └── strategy_base.{cpp,py}
|   │   ├── strategy_b/
|   │   │   ├── __init__.py
|   │   │   ├── live.cpp
|   │   │   ├── live.py
|   │   │   ├── config.yaml
|   │   │   ├── data_collector.cpp
|   │   │   ├── data_collector.hpp
|   │   │   ├── preprocessor.cpp
|   │   │   ├── preprocessor.hpp
|   │   │   ├── backtesting.cpp
|   │   │   ├── backtesting.hpp
|   │   │   ├── research.cpp
|   │   │   ├── research.hpp
|   │   │   └── strategy_base.{cpp,py}
|   │   └── ...
|   ├── interop/
|   │   └── shared_memory_comm.py
|   ├── common/
|   │   ├── base_components/
|   │   │   ├── base_data_collector.hpp
|   │   │   ├── base_data_collector.cpp
|   │   │   ├── base_preprocessor.hpp
|   │   │   ├── base_preprocessor.cpp
|   │   │   ├── base_backtesting.hpp
|   │   │   ├── base_backtesting.cpp
|   │   │   ├── base_research.hpp
|   │   │   └── base_research.cpp
|   │   ├── config.cpp
|   │   ├── config.py
|   │   ├── logger.cpp
|   │   ├── logger.py
|   │   ├── trading_calculations.cpp
|   │   ├── trading_calculations.py
|   │   ├── feature_engineering.cpp
|   │   └── feature_engineering.py
|   ├── tests/
|   │   ├── test_data_manager.cpp
|   │   ├── test_order_manager.cpp
|   │   ├── test_strategies.cpp
|   │   ├── test_risk_manager.cpp
|   │   ├── test_account_manager.cpp
|   │   └── test_data_manager.py
├── main.cpp
├── main.py
└── README.md
