# vllm-project/vllm#12080: [RFC]: BatchLLM for better shared prefix utilizing in offline scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#12080](https://github.com/vllm-project/vllm/issues/12080) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | attention;kernel;quantization;sampling;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: BatchLLM for better shared prefix utilizing in offline scenarios

### Issue 正文摘录

### Motivation. This request is mainly for **offline inference scenarios** , based on the paper [BatchLLM](https://arxiv.org/abs/2412.03594) **TL; DR:** Currently, vllm performs implicit (or _just_in_time_) shared prefix identifying and metadata collecting, and then performs cascade attention when there's one single shared prefix for all requests, according to the PR [#11635](https://github.com/vllm-project/vllm/pull/11635/files#diff-80ee7e2a62f9dcfbb8a312dc4e3948557e97ef187290daebbcae1e28596bda29). However it does not utilize the shared prefix fully under offline scenarios, where there're a lot of requests with **different** shared prefixes. This PR tries to alleviate the following pain points of vllm's inference . - Point 1: Currently vllm's inference with prefix-caching and cascade attention cannot gather all requests with the same common prefix **together** (it's essential since all query tokens with the same common prefix have to be treated as if they are from the same request, for [the attention calculation](https://github.com/vllm-project/vllm/blob/8b3291d623247c39476a09b85547629c05e04d0a/vllm/v1/worker/gpu_model_runner.py#L373C12-L379C52)) - Point 2: Under offline scenario...

## 现有链接修复摘要

#11635 [V1] Implement Cascade Attention

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s://arxiv.org/abs/2412.03594) **TL; DR:** Currently, vllm performs implicit (or _just_in_time_) shared prefix identifying and metadata collecting, and then performs cascade attention when there's one single shared prefi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ow for the performance improvement** - model: llama-3.1-8b - GPU: single A100 - setting: - no cuda_graph & multi-step decoding - for the vllm baseline, chunked-prefill(max_tokens in one batch is 2048) & prefix-caching a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e_path or "70b" in engine_path: print("70B ") kwargs ={"quantization":"gptq", "max_model_len":8192 } # os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = 1 if chunk: pipe = LLM(model=engine_path,
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: vllm performs implicit (or _just_in_time_) shared prefix identifying and metadata collecting, and then performs cascade attention when there's one single shared prefix for all requests, according to the PR [#11635](http...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: C]: BatchLLM for better shared prefix utilizing in offline scenarios RFC;stale ### Motivation. This request is mainly for **offline inference scenarios** , based on the paper [BatchLLM](https://arxiv.org/abs/2412.03594)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#11635](https://github.com/vllm-project/vllm/pull/11635) | mentioned | 0.45 | [V1] Implement Cascade Attention | enabled, and ~~cascade inference v1 is enabled default after the pr #11635~~ (found that it needs the "vllm_use_v1", add the experiment too.) - 6400 requests, each 400 of them sha… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
