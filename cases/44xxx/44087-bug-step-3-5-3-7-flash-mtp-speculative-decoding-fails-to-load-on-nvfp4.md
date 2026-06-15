# vllm-project/vllm#44087: [Bug]: Step-3.5/3.7-Flash MTP speculative decoding fails to load on NVFP4 (drafter quantizes mtp_block, can't keep unquantized MTP weights)

| 字段 | 值 |
| --- | --- |
| Issue | [#44087](https://github.com/vllm-project/vllm/issues/44087) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | fp8;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Step-3.5/3.7-Flash MTP speculative decoding fails to load on NVFP4 (drafter quantizes mtp_block, can't keep unquantized MTP weights)

### Issue 正文摘录

### Summary On an **NVFP4** checkpoint, Step-3.5/3.7-Flash **MTP speculative decoding fails to load the draft model** with an `AssertionError` (weight shape mismatch), because the MTP drafter builds its `mtp_block` (and `shared_head`) using the model's NVFP4 quant config **even when the MTP weights are unquantized (BF16)**. The draft model's quant config is filtered to the *target* model's modules, so `hf_quant_config.json` `exclude_modules` cannot reach the MTP layers — there is no way to keep them unquantized. Distinct from the existing Step-3.5 MTP issues (#38339 low acceptance, #40000 v0.19 start failure, #38498 ROCm): this is an **NVFP4-specific** quantization/load mismatch. ### Where `vllm/model_executor/models/step3p5_mtp.py`, `Step3p5AMultiTokenPredictorLayer.__init__`: ```python quant_config = vllm_config.quant_config ... self.shared_head = SharedHead(config=config, quant_config=quant_config) self.mtp_block = Step3p5DecoderLayer( vllm_config, # carries the NVFP4 quant_config prefix=f"{prefix}.mtp_block", ) ``` So `mtp_block`'s linears are created as NVFP4 (packed) and expect packed FP4 weights, while a checkpoint whose MTP block is unquantized (BF16) provides full-width w...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Step-3.5/3.7-Flash MTP speculative decoding fails to load on NVFP4 (drafter quantizes mtp_block, can't keep unquantized MTP weights) ### Summary On an **NVFP4** checkpoint, Step-3.5/3.7-Flash **MTP speculative de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t, Step-3.5/3.7-Flash **MTP speculative decoding fails to load the draft model** with an `AssertionError` (weight shape mismatch), because the MTP drafter builds its `mtp_block` (and `shared_head`) using the model's NVF...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ith an `AssertionError` (weight shape mismatch), because the MTP drafter builds its `mtp_block` (and `shared_head`) using the model's NVFP4 quant config **even when the MTP weights are unquantized (BF16)**. The draft mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fails to load the draft model** with an `AssertionError` (weight shape mismatch), because the MTP drafter builds its `mtp_block` (and `shared_head`) using the model's NVFP4 quant config **even when the MTP weights are u...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: h MTP speculative decoding fails to load on NVFP4 (drafter quantizes mtp_block, can't keep unquantized MTP weights) ### Summary On an **NVFP4** checkpoint, Step-3.5/3.7-Flash **MTP speculative decoding fails to load the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
