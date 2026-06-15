# vllm-project/vllm#44091: AMD Development Roadmap (2026 Q3)

| 字段 | 值 |
| --- | --- |
| Issue | [#44091](https://github.com/vllm-project/vllm/issues/44091) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> AMD Development Roadmap (2026 Q3)

### Issue 正文摘录

# AMD Development Roadmap (2026 Q3) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD vLLM roadmap deck (2026-05-29).* *Contributions and feedback are welcome.* > **⚠️ Draft / work-in-progress.** This roadmap is a draft and may still be updated. Items, owners, linked tickets, and dates are tentative and subject to change. This is the ROCm counterpart to the overall [vLLM Roadmap Q2 2026](https://github.com/vllm-project/vllm/issues/39749) and the [DeepSeek V4 roadmap](https://github.com/vllm-project/vllm/issues/40902). Legend: ✓ done · ▶ in progress · ○ planned. Each item links a tracked vLLM issue/PR. ## Focus - **Day-0 enablement template**: A repeatable path so the next DeepSeek / Llama / Qwen drop lands on ROCm at launch. - **Decode parity**: Match SGLang / ATOM decode at concurrency 128/512 on MI355X. - **vLLM V1 engine migration**: Move ROCm backends onto the new engine API; harden disagg. - **Public no-regression coverage**: Promote the regression CI to a public-facing dashboard with auto-gating. ## Feature and Performance Improvements (Next · Q3) - **Models** PoC: @tjtanaa @ChuanLi...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: eported in #42876 (v0.21.0 claims support but MI350X fails) - ○ DSv4 FP8 base on MI300X - ○ Stand up a day-0 enablement template (next DeepSeek / Llama / Qwen) - ○ Kimi-Linear 64M-ctx upstream · enable >100M-ctx long-co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 026 Q3) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD vLLM roadmap deck (2026-05-29).* *Contributions and feedback are we...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ress.** This roadmap is a draft and may still be updated. Items, owners, linked tickets, and dates are tentative and subject to change. This is the ROCm counterpart to the overall [vLLM Roadmap Q2 2026](https://github.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: AMD Development Roadmap (2026 Q3) rocm # AMD Development Roadmap (2026 Q3) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ○ Decode parity @ conc 128/512 vs SGLang / ATOM on MI355X - ○ FlyDSL MoE a8w4 replaces torch matmul_ogs - ○ Add DSv4 decode perf to nightly vs SGLang - ○ Tune NVFP4 / MXFP4 quant perf - ○ Cross-node TP=16 + KV-offload -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
