# vllm-project/vllm#41207: [Bug]: MM accuracy issue caused by transformers upgrade

| 字段 | 值 |
| --- | --- |
| Issue | [#41207](https://github.com/vllm-project/vllm/issues/41207) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MM accuracy issue caused by transformers upgrade

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug @hmellor We found some MM accuracy issues caused by code changes for recent transformers upgrade, like #38247. Below are reproduce steps for `Deepseek-OCR` on A100. ``` Server: VLLM_WORKER_MULTIPROC_METHOD=spawn python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-OCR --enforce-eager --port 8023 --host 0.0.0.0 --trust-remote-code --gpu-memory-util=0.95 --no-enable-prefix-caching --max-num-batched-tokens=8192 --max-model-len=8192 --block-size 64 Client: curl http://0.0.0.0:8023/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "deepseek-ai/DeepSeek-OCR", "temperature":0, "messages": [ { "role": "user", "content": [ { "type": "text", "text": "describe the image" }, { "type": "image_url", "image_url": { "url": "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg" } } ] } ], "max_tokens": 512 }' ``` Output: ``` {"id":"chatcmpl-b16af1a23c1cbb45","object":"chat.completion","created":1777383662,"model":"deepseek-ai/DeepSeek-OCR","choices":[{"index":0,"message":{"role":"assistant","content":"ThisĠimageĠdisplaysĠaĠduckĠinĠtheĠforeground,ĠwithĠaĠbodyĠofĠwaterĠinĠtheĠbac...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _MULTIPROC_METHOD=spawn python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-OCR --enforce-eager --port 8023 --host 0.0.0.0 --trust-remote-code --gpu-memory-util=0.95 --no-enable-prefix-caching --m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in a body of water. The duck is positioned in the center of the image, facing to the right. It has a green head, a yellow beak, and a brown body with white and black markings. The water is calm with gentle ripples, refl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rs upgrade, like #38247. Below are reproduce steps for `Deepseek-OCR` on A100. ``` Server: VLLM_WORKER_MULTIPROC_METHOD=spawn python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-OCR --enforce-eage...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: MM accuracy issue caused by transformers upgrade bug ### Your current environment ### 🐛 Describe the bug @hmellor We found some MM accuracy issues caused by code changes for recent transformers upgrade, like #382...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ble-prefix-caching --max-num-batched-tokens=8192 --max-model-len=8192 --block-size 64 Client: curl http://0.0.0.0:8023/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "deepseek-ai/DeepSeek-OCR", "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
