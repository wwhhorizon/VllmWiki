# vllm-project/vllm#11626: [Bug]: When I use vllm to start deepseek-ai/DeepSeek-V2-Lite-Chat model inference, the error "deepseek-ai/DeepSeek-V2-Lite-Chat" is reported. My vllm version is 0.6.3，help me bro

| 字段 | 值 |
| --- | --- |
| Issue | [#11626](https://github.com/vllm-project/vllm/issues/11626) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When I use vllm to start deepseek-ai/DeepSeek-V2-Lite-Chat model inference, the error "deepseek-ai/DeepSeek-V2-Lite-Chat" is reported. My vllm version is 0.6.3，help me bro

### Issue 正文摘录

### Your current environment ### Model Input Dumps error log [err_execute_model_input_20241230-104114.pkl.zip](https://github.com/user-attachments/files/18274183/err_execute_model_input_20241230-104114.pkl.zip) ### 🐛 Describe the bug When I use vllm to start deepseek-ai/DeepSeek-V2-Lite-Chat model inference, the error "deepseek-ai/DeepSeek-V2-Lite-Chat" is reported. My vllm version is 0.6.3，My startup command: CUDA_VISIBLE_DEVICES=1,4,5,6 python -m vllm.entrypoints.openai.api_server --model /workspace/pretrained/ --port 10000 --tensor-parallel-size 4 --gpu-memory- utilization 0.95 --max-model-len 1024 --trust-remote-code --enforce_eager --dtype=half 。help me bro ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ence, the error "deepseek-ai/DeepSeek-V2-Lite-Chat" is reported. My vllm version is 0.6.3，help me bro bug;stale ### Your current environment ### Model Input Dumps error log [err_execute_model_input_20241230-104114.pkl.z...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lization 0.95 --max-model-len 1024 --trust-remote-code --enforce_eager --dtype=half 。help me bro ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot livin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -V2-Lite-Chat" is reported. My vllm version is 0.6.3，My startup command: CUDA_VISIBLE_DEVICES=1,4,5,6 python -m vllm.entrypoints.openai.api_server --model /workspace/pretrained/ --port 10000 --tensor-parallel-size 4 --g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Seek-V2-Lite-Chat" is reported. My vllm version is 0.6.3，help me bro bug;stale ### Your current environment ### Model Input Dumps error log [err_execute_model_input_20241230-104114.pkl.zip](https://github.com/user-attac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;quantization;speculative_decoding cuda;operator;quantization;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
