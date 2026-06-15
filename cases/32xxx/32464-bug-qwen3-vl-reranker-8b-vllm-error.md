# vllm-project/vllm#32464: [Bug]: Qwen3-VL-Reranker-8B vllm error

| 字段 | 值 |
| --- | --- |
| Issue | [#32464](https://github.com/vllm-project/vllm/issues/32464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Reranker-8B vllm error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is my script for serving vllm, which is adapted from [vision_rerank_api_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py): ``` vllm serve local/path/to/Qwen/Qwen3-VL-Reranker-8B \ --served-model-name Qwen3-VL-Reranker-8B \ --host 0.0.0.0 \ --runner pooling \ --max-model-len 8192 \ --gpu_memory_utilization 0.6 \ --trust-remote-code \ --chat-template local/path/to/vllm/examples/pooling/score/template/qwen3_vl_reranker.jinja ``` Here is my script for using reranker ``` import json import requests headers = {"accept": "application/json", "Content-Type": "application/json"} query = "A woman playing with her dog on a beach at sunset." documents = { "content": [ { "type": "text", "text": ( "A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset, " # noqa: E501 "as the dog offers its paw in a heartwarming display of companionship and trust." # noqa: E501 ), }, { "type": "image_url", "image_url": { "url": image_base64_data }, }, ] } def main(): rerank_url = "http://localhost:port/v1/rerank" model = 'Qwen3-VL-Reranker-8B' data = { "model":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: te/qwen3_vl_reranker.jinja ``` Here is my script for using reranker ``` import json import requests headers = {"accept": "application/json", "Content-Type": "application/json"} query = "A woman playing with her dog on a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: "as the dog offers its paw in a heartwarming display of companionship and trust." # noqa: E501 ), }, { "type": "image_url", "image_url": { "url": image_base64_data }, }, ] } def main(): re
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-Reranker-8B vllm error bug ### Your current environment ### 🐛 Describe the bug Here is my script for serving vllm, which is adapted from [vision_rerank_api_online.py](https://github.com/vllm-project/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r.jinja ``` Here is my script for using reranker ``` import json import requests headers = {"accept": "application/json", "Content-Type": "application/json"} query = "A woman playing with her dog on a beach at sunset."...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
