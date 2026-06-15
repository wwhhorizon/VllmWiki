# vllm-project/vllm#5983: [Bug]: TypeError: FlashAttentionMetadata.__init__() missing 10 required positional arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#5983](https://github.com/vllm-project/vllm/issues/5983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: FlashAttentionMetadata.__init__() missing 10 required positional arguments

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT error： python -m vllm.entrypoints.openai.api_server --model /ai/LLaVA-NeXT --image-token-id 32000 --image-input-shape 1,3,336,336 --image-input-type pixel_values --image-feature-size 65856 --chat-template template_llava.jinja --host 19*** --port 10860 --trust-remote-code --tensor-parallel-size 2 --dtype=half --disable-custom-all-reduce ![image](https://github.com/vllm-project/vllm/assets/40717349/70d6a8e0-fcf6-425a-85a8-52854b9dabbf)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: TypeError: FlashAttentionMetadata.__init__() missing 10 required positional arguments bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT error...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ost 19*** --port 10860 --trust-remote-code --tensor-parallel-size 2 --dtype=half --disable-custom-all-reduce ![image](https://github.com/vllm-project/vllm/assets/40717349/70d6a8e0-fcf6-425a-85a8-52854b9dabbf)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: TypeError: FlashAttentionMetadata.__init__() missing 10 required positional arguments bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug run LLaVA-NeXT error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g run LLaVA-NeXT error： python -m vllm.entrypoints.openai.api_server --model /ai/LLaVA-NeXT --image-token-id 32000 --image-input-shape 1,3,336,336 --image-input-type pixel_values --image-feature-size 65856 --chat-templa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
