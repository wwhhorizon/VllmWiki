# vllm-project/vllm#23615: [Bug]: vllm运行Qwen3 reranker准确性问题

| 字段 | 值 |
| --- | --- |
| Issue | [#23615](https://github.com/vllm-project/vllm/issues/23615) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm运行Qwen3 reranker准确性问题

### Issue 正文摘录

### Your current environment **1.使用vllm0.9.2版本执行以下命令报错tensor不匹配** CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-parallel-size 4 --trust-remote-code --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"],"classifier_from_token":["no","yes"],"is_original_qwen3_reranker": true}' **2.使用vllm0.9.2版本执行以下命令出现准确性极差的问题** CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-parallel-size 4 --trust-remote-code 3.使用vllm0.10.0版本执行以下命令后，发送post请求没有任何反馈，后台仅显示added request rerank CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-parallel-size 4 --trust-remote-code --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"],"classifier_from_token":["no","yes"],"is_original_qwen3_reranker": true}' ### 🐛 Describe the bug vllm在命令行运行qwen3 reranker的诸多问题 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm运行Qwen3 reranker准确性问题 bug ### Your current environment **1.使用vllm0.9.2版本执行以下命令报错tensor不匹配** CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug ### Your current environment **1.使用vllm0.9.2版本执行以下命令报错tensor不匹配** CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-parallel-size 4 --trust-remote-co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 4 --trust-remote-code 3.使用vllm0.10.0版本执行以下命令后，发送post请求没有任何反馈，后台仅显示added request rerank CUDA_VISIABLE_DEVICES=0,1,2,3 vllm serve ./model/Qwen3-reranker-8B --host 0.0.0.0 --port 8000 --task score --tensor-parallel-size 4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
