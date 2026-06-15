# vllm-project/vllm#20158: [CI Failure]: `deepseek_mtp_main_random_bf16` can't load, causes deepseek_mtp CI Failure.

| 字段 | 值 |
| --- | --- |
| Issue | [#20158](https://github.com/vllm-project/vllm/issues/20158) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: `deepseek_mtp_main_random_bf16` can't load, causes deepseek_mtp CI Failure.

### Issue 正文摘录

### Name of failing test `https://github.com/vllm-project/vllm-ascend/actions/runs/15890661413/job/44812465270?pr=1128` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `Acsend 910b platform` `pytest ./tests/e2e/long_term/spec_decode_v0/e2e/test_mtp_correctness.py` ### 📝 History of failing test ```bash vllm-empty/vllm/model_executor/model_loader/default_loader.py:269: in load_weights loaded_weights = model.load_weights( _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ self = CustomDeepSeekMTP( (model): CustomDeepSeekMultiTokenPredictor( (layers): ModuleDict( (5): CustomDeepSeekMu...ogitsProcessor(vocab_size=129280, org_vocab_size=129280, scale=1.0, logits_as_input=False) ) (sampler): Sampler() ) weights = def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]: stacked_params_mapping = [ ("gate_up_proj", "gate_proj", 0), ("gate_up_proj", "up_proj", 1), ] expert_params_mapping = FusedMoE.make_expert_params_mapping( ckpt_gate_proj_name="gate_proj", ckpt_down_proj_name="down_proj", ckpt_up_proj_name="up_proj", num_exp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm-ascend/actions/runs/15890661413/job/44812465270?pr=1128` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [CI Failure]: `deepseek_mtp_main_random_bf16` can't load, causes deepseek_mtp CI Failure. stale;ci-failure ### Name of failing test `https://github.com/vllm-project/vllm-ascend/actions/runs/15890661413/job/44812465270?p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r(vocab_size=129280, org_vocab_size=129280, scale=1.0, logits_as_input=False) ) (sampler): Sampler() ) weights = def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]: stacked_params_mapping = [
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: , 0), ("gate_up_proj", "up_proj", 1), ] expert_params_mapping = FusedMoE.make_expert_params_mapping( ckpt_gate_proj_name="gate_proj", ckpt_down_proj_name="down_proj", ckpt_up_proj_name="up_proj", num_experts=self
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: epseek_mtp_main_random_bf16` can't load, causes deepseek_mtp CI Failure. stale;ci-failure ### Name of failing test `https://github.com/vllm-project/vllm-ascend/actions/runs/15890661413/job/44812465270?pr=1128` ### Basic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
