# vllm-project/vllm#43894: [Bug] V1 InputBatch condense can leak stale allowed_token_ids mask to recycled row

| 字段 | 值 |
| --- | --- |
| Issue | [#43894](https://github.com/vllm-project/vllm/issues/43894) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] V1 InputBatch condense can leak stale allowed_token_ids mask to recycled row

### Issue 正文摘录

## Summary In current `main` (`4bfa0f2b1458be320fa39c6fa54be5f83cef2444`), V1 `InputBatch.condense()` can leave a stale `allowed_token_ids_mask_cpu_tensor` row behind after moving a constrained request down. A later unrestricted request can reuse that old row because `add_request()` only writes `allowed_token_ids_mask_cpu_tensor[req_index]` when `sampling_params.allowed_token_ids` is set. When another active request still has `allowed_token_ids`, `_make_sampling_metadata()` copies the active prefix of the CPU mask to GPU and `Sampler.apply_logits_processors()` applies the stale whitelist to the unrestricted request. ## Duplicate search I searched open issues and PRs in `vllm-project/vllm` for: - `allowed_token_ids_mask condense` - `allowed_token_ids stale InputBatch` - `allowed_token_ids dynamic batching` - `allowed_token_ids recycled row` No open issue or PR hits were returned by GitHub search for those queries. ## Environment - GCP VM: `a2-highgpu-1g`, 1x `NVIDIA A100-SXM4-40GB` - Zone: `us-central1-a` - Driver: `580.159.03` - vLLM source: `4bfa0f2b1458be320fa39c6fa54be5f83cef2444` - vLLM version: `0.1.dev1+g4bfa0f2b1` - PyTorch: `2.11.0+cu130` - CUDA visible: `True`, GPU name `...

## 现有链接修复摘要

#43931 [Bugfix] V1: clear stale allowed_token_ids mask in InputBatch.condense

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 159.03` - vLLM source: `4bfa0f2b1458be320fa39c6fa54be5f83cef2444` - vLLM version: `0.1.dev1+g4bfa0f2b1` - PyTorch: `2.11.0+cu130` - CUDA visible: `True`, GPU name `NVIDIA A100-SXM4-40GB` - Install mode: editable source...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: applies the stale whitelist to the unrestricted request. ## Duplicate search I searched open issues and PRs in `vllm-project/vllm` for: - `allowed_token_ids_mask condense` - `allowed_token_ids stale InputBatch` - `allow...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _server --model facebook/opt-125m --host 127.0.0.1 --port 8000 --dtype float16 --max-num-seqs 8 --max-model-len 2048 --gpu-memory-utilization 0.25 --enforce-eager ``` Client command: ```bash python repro_server_allowed_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: en another active request still has `allowed_token_ids`, `_make_sampling_metadata()` copies the active prefix of the CPU mask to GPU and `Sampler.apply_logits_processors()` applies the stale whitelist to the unrestricte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] V1 InputBatch condense can leak stale allowed_token_ids mask to recycled row ## Summary In current `main` (`4bfa0f2b1458be320fa39c6fa54be5f83cef2444`), V1 `InputBatch.condense()` can leave a stale `allowed_token_i...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43931](https://github.com/vllm-project/vllm/pull/43931) | closes_keyword | 0.95 | [Bugfix] V1: clear stale allowed_token_ids mask in InputBatch.condense | Fixes #43894. `InputBatch.condense()` copies `allowed_token_ids_mask_cpu_tensor` from a moved request's row into the freed index but never clears the source row. `add_request` o |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
