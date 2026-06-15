# vllm-project/vllm#20464: [Bug]: Repeat my input prompt as the output

| 字段 | 值 |
| --- | --- |
| Issue | [#20464](https://github.com/vllm-project/vllm/issues/20464) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Repeat my input prompt as the output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 我的测试环境是： - Docker：vllm/vllm-openai:latest - 8张 a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/models/:/data/models/ \ -p 18000:18000 \ --ipc=host \ vllm/vllm-openai:latest \ --model /data/models/DeepSeek-R1-Distill-Qwen-32B \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 18000 ``` 发送请求， ```text curl http://localhost:18000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/data/models/DeepSeek-R1-Distill-Qwen-32B", "prompt": "西游记中谁最厉害", "max_tokens": 4096, "temperature": 0 }' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug 我的测试环境是： - Docker：vllm/vllm-openai:latest - 8张 a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/models/:/data/models/ \ -p 18000:18000 \ --ipc=host \ vllm/vllm-openai:latest \ --m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/models/:/data/models/ \ -p 18000:18000 \ --ipc=host \ vllm/vllm-openai:latest \ --model /data/models/DeepSeek-R1-Distill-Qwen-32B \ --tensor-parallel-siz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Your current environment ### 🐛 Describe the bug 我的测试环境是： - Docker：vllm/vllm-openai:latest - 8张 a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/models/:/data/models/ \ -p 18000:18000 \ --ipc=host \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Repeat my input prompt as the output bug;stale ### Your current environment ### 🐛 Describe the bug 我的测试环境是： - Docker：vllm/vllm-openai:latest - 8张 a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ent ### 🐛 Describe the bug 我的测试环境是： - Docker：vllm/vllm-openai:latest - 8张 a100 NVIDIA GPU 运行的命令是： ```shell docker run --gpus all \ -v /data/models/:/data/models/ \ -p 18000:18000 \ --ipc=host \ vllm/vllm-openai:latest \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
