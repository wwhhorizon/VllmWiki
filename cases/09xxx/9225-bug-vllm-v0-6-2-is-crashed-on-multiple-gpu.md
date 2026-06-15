# vllm-project/vllm#9225: [Bug]: vllm v0.6.2 is crashed on multiple GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#9225](https://github.com/vllm-project/vllm/issues/9225) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm v0.6.2 is crashed on multiple GPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO: Started server process [11912] INFO: Waiting for application startup. INFO: Application startup complete. ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8080): address already in use INFO: Waiting for application shutdown. INFO: Application shutdown complete. My command to start vllm: ``` python3 -m vllm.entrypoints.openai.api_server --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --host 0.0.0.0 --port 8080 --seed 42 --trust-remote-code --disable-frontend-multiprocessing \ --enable-chunked-prefill --tensor-parallel-size 2 --max-model-len 98304 >> "$LOG_FILE" 2>&1 & ``` If I change tensor-parallel-size from 2 to 1, no such issue. docker image in use is "vllm/vllm-openai:v0.6.2". ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: vllm: ``` python3 -m vllm.entrypoints.openai.api_server --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --host 0.0.0.0 --port 8080 --seed 42 --trust-remote-code --disable-frontend-multiprocessing \ --enabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .6.2 is crashed on multiple GPU bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug INFO: Started server process [11912] INFO: Waiting for application startup. INFO: Application s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: # 🐛 Describe the bug INFO: Started server process [11912] INFO: Waiting for application startup. INFO: Application startup complete. ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8080): address...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: >&1 & ``` If I change tensor-parallel-size from 2 to 1, no such issue. docker image in use is "vllm/vllm-openai:v0.6.2". ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2". ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
