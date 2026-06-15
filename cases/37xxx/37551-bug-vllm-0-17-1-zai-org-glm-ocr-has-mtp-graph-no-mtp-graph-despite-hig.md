# vllm-project/vllm#37551: [Bug] vLLM 0.17.1: `zai-org/GLM-OCR` has `mtp_graph < no_mtp_graph` despite high acceptance

| 字段 | 值 |
| --- | --- |
| Issue | [#37551](https://github.com/vllm-project/vllm/issues/37551) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] vLLM 0.17.1: `zai-org/GLM-OCR` has `mtp_graph < no_mtp_graph` despite high acceptance

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For `zai-org/GLM-OCR`, I observe: - `mtp_eager > no_mtp_eager` (expected) - but `mtp_graph 1 else 0.0, "runs": tps, } return out all_res = {} for mode, cfg in MODES.items(): print(f"Running mode={mode}") all_res[mode] = run_mode(cfg) print("\n=== RESULTS (tok/s) ===") for image in IMAGES: ne = all_res["no_mtp_eager"][image]["avg"] ng = all_res["no_mtp_graph"][image]["avg"] me = all_res["mtp_eager"][image]["avg"] mg = all_res["mtp_graph"][image]["avg"] print( f"{image}: no_mtp_eager={ne:.2f}, no_mtp_graph={ng:.2f}, " f"mtp_eager={me:.2f}, mtp_graph={mg:.2f}, " f"mtp_eager/no_mtp_eager={me/ne:.3f}x, " f"mtp_graph/no_mtp_graph={mg/ng:.3f}x" ) print("\nRAW_JSON") print(json.dumps(all_res, indent=2)) ``` ## Observed result In my runs on v0.17.1: - `receipt` - `no_mtp_eager`: 60.082 tok/s - `no_mtp_graph`: 465.308 tok/s - `mtp_eager`: 91.792 tok/s (`1.528x` vs no_mtp_eager) - `mtp_graph`: 260.372 tok/s (`0.560x` vs no_mtp_graph) - mtp_graph acceptance: ~69%, mean acceptance length ~1.69 - `ocr_demo` - `no_mtp_eager`: 59.479 tok/s - `no_mtp_graph`: 397.387 tok/s - `mtp_eager`: 90.687 tok/s (`1.525x` vs no_mtp_eager) - `mtp_graph`: 277.2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;triton build_error;slowdown dtype;env_dependency...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed questions. performance ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;triton build_error;slowdown dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: allel;hardware_porting;model_support;multimodal_vlm;sampling_logits cuda;triton build_error;slowdown dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: _support;multimodal_vlm;sampling_logits cuda;triton build_error;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
