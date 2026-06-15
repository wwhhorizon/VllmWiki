# vllm-project/vllm#34406: [Bug]: Instruction following capability is deteriorating：Output introduces parameter  defined in functioncall incorrectly

| 字段 | 值 |
| --- | --- |
| Issue | [#34406](https://github.com/vllm-project/vllm/issues/34406) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Instruction following capability is deteriorating：Output introduces parameter  defined in functioncall incorrectly

### Issue 正文摘录

### Your current environment ``` GPU：H100 Driver Version: 580.105.08 CUDA Version: 13.0 vLLM version：0.14.1 ``` ### Service pull-up command: ``` vllm serve /data1/Qwen/Qwen3-32B \ --served-model-name "Qwen3-32B" \ --tensor-parallel-size 4 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory-utilization 0.8 \ --max-model-len 32768 \ --port 1025 ``` ### curl prompts attachment: [test2.json](https://github.com/user-attachments/files/25254247/test2.json) ### 🐛 Describe the bug Execute curl command，the output is as follows: ``` {"id":"chatcmpl-a794a3c992dbd018","object":"chat.completion","created":1770806370,"model":"Qwen3-32B","choices":[{"index":0,"message":{"role":"assistant","content":"","refusnnotations":null,"audio":null,"function_call":null,"tool_calls":[{"id":"chatcmpl-tool-9ee44cce68901374","type":"function", "function":{"name":"planning","arguments":"{\"step_"not_started\", \"step_notes\": \"\", \"step_index\": 0, \"title\": \"黄金价格趋势分析\", \"steps\": [\"执行顺序1. 数据收集：从可靠来源获取黄金价格历史数据\", \"执行顺序2. 趋用分析工具识别黄金价格的长期趋势和周期性波动\", \"执行顺序3. 影响因素分析：分析宏观经济指标（如通货膨胀、利率、美元指数）对黄金价格的影响\", \"执行顺序4. 报告总结：整理分析结页版报告\"], \"command\": \"create\"}"}}], "reasoning":null,"reasoning_conte...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Instruction following capability is deteriorating：Output introduces parameter defined in functioncall incorrectly bug;stale ### Your current environment ``` GPU：H100 Driver Version: 580.105.08 CUDA Version: 13.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: incorrectly bug;stale ### Your current environment ``` GPU：H100 Driver Version: 580.105.08 CUDA Version: 13.0 vLLM version：0.14.1 ``` ### Service pull-up command: ``` vllm serve /data1/Qwen/Qwen3-32B \ --served-model-na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LM version：0.14.1 ``` ### Service pull-up command: ``` vllm serve /data1/Qwen/Qwen3-32B \ --served-model-name "Qwen3-32B" \ --tensor-parallel-size 4 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing：Output introduces parameter defined in functioncall incorrectly bug;stale ### Your current environment ``` GPU：H100 Driver Version: 580.105.08 CUDA Version: 13.0 vLLM version：0.14.1 ``` ### Service pull-up command:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --max-model-len 32768 \ --port 1025 ``` ### curl prompts attachment: [test2.json](https://github.com/user-attachments/files/25254247/test2.json) ### 🐛 Describe the bug Execute curl command，the output is as follows: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
