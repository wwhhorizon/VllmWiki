# vllm-project/vllm#21672: [Usage]: Logits processor with v1

| 字段 | 值 |
| --- | --- |
| Issue | [#21672](https://github.com/vllm-project/vllm/issues/21672) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Logits processor with v1

### Issue 正文摘录

### Your current environment Hello everyone, I can't find an example on how to use the new logits processor class for vllm v1. I want to build something that probably look like this with the old framework: It should work similar to guided decoding. ``` def process_token(token_ids, logits): for i, token_id in enumerate(token_ids): # print(f"Token ID: {token_id}, Logit: {logits[i]}") if token_id not in [ self.tokenizer.encode("no", add_special_tokens=False)[0], self.tokenizer.encode("oth", add_special_tokens=False)[0], self.tokenizer.encode("Ak", add_special_tokens=False)[0], self.tokenizer.encode("Pas", add_special_tokens=False)[0], self.tokenizer.encode("Gu", add_special_tokens=False)[0] ]: logits[i] = -np.inf return logits ``` I try to achieve this because I'm searching for the different behaviour in the predictions of vllm with guided decoding vs transformers with prefix_allowed_tokens_fn. I describe the case in the [gemma3-27b-it repositoory](https://huggingface.co/google/gemma-3-27b-it/discussions/70#6881317792a7d591385c618f). I hope you can help me with an example or an idea why the classification with Guided Decoding in vllm performs so much wore that the transformers approa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: mple on how to use the new logits processor class for vllm v1. I want to build something that probably look like this with the old framework: It should work similar to guided decoding. ``` def process_token(token_ids, l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: p.inf return logits ``` I try to achieve this because I'm searching for the different behaviour in the predictions of vllm with guided decoding vs transformers with prefix_allowed_tokens_fn. I describe the case in the [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: transformers with prefix_allowed_tokens_fn. I describe the case in the [gemma3-27b-it repositoory](https://huggingface.co/google/gemma-3-27b-it/discussions/70#6881317792a7d591385c618f). I hope you can help me with an ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Logits processor with v1 usage;stale ### Your current environment Hello everyone, I can't find an example on how to use the new logits processor class for vllm v1. I want to build something that probably look l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.6.post1+cu128torch2.7 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.3.14 [pip3] nvidia-cuda-cupti-cu12==12.8.57 [pip3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
