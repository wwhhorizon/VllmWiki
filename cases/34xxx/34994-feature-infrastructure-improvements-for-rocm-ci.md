# vllm-project/vllm#34994: [Feature]: Infrastructure Improvements for ROCm CI

| 字段 | 值 |
| --- | --- |
| Issue | [#34994](https://github.com/vllm-project/vllm/issues/34994) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Infrastructure Improvements for ROCm CI

### Issue 正文摘录

cc @kenroche ## General - [ ] Enable `grade: Blocking` for all tests on amd-ci pipeline - [ ] Mirror all tests on upstream CI pipeline - [x] Tailor the "V1 Test attention" test group to MI325 and MI355 respecitvely - [x] Fix Moriio tests in `v1/kv_connector/unit/test_moriio_connector.py` - [ ] Enable Moriio tests on upstream -- infra related issue - [x] Add FP4 tests for `GPQA Eval (GPT-OSS) (B200-MI355)` and maybe alternative quantization or attention backend tests for `GPQA Eval (GPT-OSS) (H100-MI325)` (e.g. AITER test). - [ ] Add back the 2 Node tests and other multi-node tests (coordinate with infra team to do that) - [ ] Fix LoRA GPT-OSS test `pytest -v -s -x lora/test_gptoss_tp.py` - [ ] Enable Marlin kernels on ROCm or a Triton LoRA-compatible attention backend - [ ] Add smart test targeting feature ## Distributed Tests - [x] Add `CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs)` support on ROCm. Currently on ROCm: `CROSS_LAYERS_BLOCKS=True ROCM_ATTN=1 bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` fails ### Distributed Tests (2 GPUs) - [ ] Remove `TORCH_NCCL_BLOCKING_WAIT=1` when HIP bug [ROCm/hip#3876](https://github.com/ROCm...

## 现有链接修复摘要

#3876 [Bugfix] handle prompt_logprobs in _apply_min_tokens_penalty | #39564 [Hardware][AMD][Bugfix] Defer ROCm GCN arch fallback to avoid forced spawn

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 11: [Feature]: Infrastructure Improvements for ROCm CI feature request;rocm cc @kenroche ## General - [ ] Enable `grade: Blocking` for all tests on amd-ci pipeline - [ ] Mirror all tests on upstream CI pipeline - [x] Tailor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: (GPT-OSS) (B200-MI355)` and maybe alternative quantization or attention backend tests for `GPQA Eval (GPT-OSS) (H100-MI325)` (e.g. AITER test). - [ ] Add back the 2 Node tests and other multi-node tests (coordinate with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature]: Infrastructure Improvements for ROCm CI feature request;rocm cc @kenroche ## General - [ ] Enable `grade: Blocking` for all tests on amd-ci pipeline - [ ] Mirror all tests on upstream CI pipeline - [x] Tailor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ` - [ ] Enable Moriio tests on upstream -- infra related issue - [x] Add FP4 tests for `GPQA Eval (GPT-OSS) (B200-MI355)` and maybe alternative quantization or attention backend tests for `GPQA Eval (GPT-OSS) (H100-MI32...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s on upstream -- infra related issue - [x] Add FP4 tests for `GPQA Eval (GPT-OSS) (B200-MI355)` and maybe alternative quantization or attention backend tests for `GPQA Eval (GPT-OSS) (H100-MI325)` (e.g. AITER test). - [...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3876](https://github.com/vllm-project/vllm/pull/3876) | mentioned | 0.45 | [Bugfix] handle prompt_logprobs in _apply_min_tokens_penalty | (a100,mi300) - [ ] remove `torch_nccl_blocking_wait=1` when hip bug [rocm/hip#3876](https://github.com/rocm/hip/issues/3876) is fixed in a future rocm release. - [ ] modify the te… |
| [#39564](https://github.com/vllm-project/vllm/pull/39564) | mentioned | 0.6 | [Hardware][AMD][Bugfix] Defer ROCm GCN arch fallback to avoid forced spawn | le ## Why this is not duplicate work I checked: - issue comments on #34994 - open PRs referencing `34994` - open PRs for `test_gptoss_tp.py` / `gptoss_tp` / ROCm LoRA GPT-OSS I di… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
