# vllm-project/vllm#5982: [Bug]: AttributeError: 'NoneType' object has no attribute 'prefill_metadata'

| 字段 | 值 |
| --- | --- |
| Issue | [#5982](https://github.com/vllm-project/vllm/issues/5982) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'NoneType' object has no attribute 'prefill_metadata'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT | llava-hf/llava-v1.6-mistral-7b-hf python -m vllm.entrypoints.openai.api_server --model /ai/LLaVA-NeXT --image-token-id 32000 --image-input-shape 1,3,336,336 --image-input-type pixel_values --image-feature-size 65856 --chat-template template_llava.jinja --host 19*** --port 10860 --trust-remote-code --tensor-parallel-size 1 --dtype=half --disable-custom-all-reduce ![image](https://github.com/vllm-project/vllm/assets/40717349/e20a7cab-5052-4f04-b960-c5426e2717f2)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: thon collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT | llava-hf/llava-v1.6-mistral-7b-hf python -m vllm.entrypoints.openai.api_server --model /ai/LLaVA-NeXT --image-token-id 32000 --image-input-shape 1,3,336,3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ost 19*** --port 10860 --trust-remote-code --tensor-parallel-size 1 --dtype=half --disable-custom-all-reduce ![image](https://github.com/vllm-project/vllm/assets/40717349/e20a7cab-5052-4f04-b960-c5426e2717f2)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT | llava-hf/llava-v1.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: AttributeError: 'NoneType' object has no attribute 'prefill_metadata' bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT | llava-hf/llava-v1.6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
