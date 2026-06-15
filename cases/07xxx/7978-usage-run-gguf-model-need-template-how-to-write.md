# vllm-project/vllm#7978: [Usage]: run gguf model need template，how to write？ 

| 字段 | 值 |
| --- | --- |
| Issue | [#7978](https://github.com/vllm-project/vllm/issues/7978) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: run gguf model need template，how to write？ 

### Issue 正文摘录

### Your current environment BadRequestError: Error code: 400 - {'object': 'error', 'message': 'As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.', 'type': 'BadRequestError', 'param': None, 'code': 400} ### How would you like to use vllm CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --host 0.0.0.0 --port 10868 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1 --dtype=half --quantization gguf --load-format gguf ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: run gguf model need template，how to write？ usage ### Your current environment BadRequestError: Error code: 400 - {'object': 'error', 'message': 'As of transformers v4.44, default chat template is no longer allo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 8 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1 --dtype=half --quantization gguf --load-format gguf ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rror', 'param': None, 'code': 400} ### How would you like to use vllm CUDA_VISIBLE_DEVICES=1 vllm serve /ai/qwen1.5-1.8b.gguf --host 0.0.0.0 --port 10868 --max-model-len 4096 --trust-remote-code --tensor-parallel-size 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: odel need template，how to write？ usage ### Your current environment BadRequestError: Error code: 400 - {'object': 'error', 'message': 'As of transformers v4.44, default chat template is no longer allowed, so you must pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
