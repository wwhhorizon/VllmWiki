# vllm-project/vllm#40000: [Bug]: Step 3.5 Flash MTP failed to start in v0.19.0

| 字段 | 值 |
| --- | --- |
| Issue | [#40000](https://github.com/vllm-project/vllm/issues/40000) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Step 3.5 Flash MTP failed to start in v0.19.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In v0.19.0 Step3.5-Flash MTP failed to start due to incorrect model config construction. Specifically, in Step3.5-Flash the model config construction has a few layers that're truncated as a result of update in #38247. Because Step3.5-Flash has the MTP block stored in the config as layers > 45 so the update removed the mtp_block's layer_types from the config construction. Causing the IndexError as shown below during server startup. config.json: ``` "num_hidden_layers": 45, ... "model.layers.45.mtp_block.self_attn.g_proj", "model.layers.45.mtp_block.self_attn.qkv_proj", "model.layers.45.mtp_block.self_attn.o_proj", "model.layers.45.mtp_block.mlp.gate_up_proj", "model.layers.45.mtp_block.mlp.down_proj", ... ``` Startup command + error: ``` vllm serve stepfun-ai/Step-3.5-Flash-FP8 --tensor-parallel-size 4 --reasoning-parser step3p5 --tool-call-parser step3p5 --enable-auto-tool-choice --trust-remote-code --disable-cascade-attn --enable-expert-parallel --hf-overrides '{"num_nextn_predict_layers": 1}' --speculative-config '{"method": "step3p5_mtp", "num_speculative_tokens": 1}' .... # Error (Worker_TP0_EP0 pid=2116241) ERROR 04-16 14:12...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Step 3.5 Flash MTP failed to start in v0.19.0 bug;rocm ### Your current environment ### 🐛 Describe the bug In v0.19.0 Step3.5-Flash MTP failed to start due to incorrect model config construction. Specifically, in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ash MTP failed to start due to incorrect model config construction. Specifically, in Step3.5-Flash the model config construction has a few layers that're truncated as a result of update in #38247. Because Step3.5-Flash...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: . ``` Startup command + error: ``` vllm serve stepfun-ai/Step-3.5-Flash-FP8 --tensor-parallel-size 4 --reasoning-parser step3p5 --tool-call-parser step3p5 --enable-auto-tool-choice --trust-remote-code --disable-cascade-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e the bug In v0.19.0 Step3.5-Flash MTP failed to start due to incorrect model config construction. Specifically, in Step3.5-Flash the model config construction has a few layers that're truncated as a result of update in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cated as a result of update in #38247. Because Step3.5-Flash has the MTP block stored in the config as layers > 45 so the update removed the mtp_block's layer_types from the config construction. Causing the IndexError a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
