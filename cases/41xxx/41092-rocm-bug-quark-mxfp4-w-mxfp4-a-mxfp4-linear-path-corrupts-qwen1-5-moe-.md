# vllm-project/vllm#41092: [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355

| 字段 | 值 |
| --- | --- |
| Issue | [#41092](https://github.com/vllm-project/vllm/issues/41092) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On ROCm `gfx950` / MI355, `fxmarty/qwen_1.5-moe-a2.7b-mxfp4` loads and runs, but greedy generation is corrupted when vLLM uses the native Quark OCP MX `w_mxfp4_a_mxfp4` linear path. Run the smoke test: ```python # /tmp/repro_quark_mxfp4_rocm.py from vllm import LLM, SamplingParams if __name__ == "__main__": llm = LLM( model="fxmarty/qwen_1.5-moe-a2.7b-mxfp4", dtype="auto", tensor_parallel_size=1, gpu_memory_utilization=0.7, enforce_eager=True, ) out = llm.generate( ["The capital of France is"], SamplingParams(temperature=0.0, max_tokens=24), )[0].outputs[0] print("text:", repr(out.text)) print("token_ids:", list(out.token_ids)) ``` ```bash python /tmp/repro_quark_mxfp4_rocm.py ``` Observed output on the native path: ```text text: '内在品质和 souhailli부面照\n形兄fr peny根本ly配方马上.Drop极动作paged准备.Marshal潭' token_ids: [108314, 102013, 33108, 76338, 57168, 63089, 27091, 99331, 198, 82699, 100788, 1626, 92933, 100232, 398, 108203, 102392, 21688, 99226, 102196, 63115, 101077, 37271, 102740] ``` Expected output should be a coherent completion about Paris. For Wikitext correctness, the existing repo test already covers this model: ```bash pytest -s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: un the smoke test: ```python # /tmp/repro_quark_mxfp4_rocm.py from vllm import LLM, SamplingParams if __name__ == "__main__": llm = LLM( model="fxmarty/qwen_1.5-moe-a2.7b-mxfp4", dtype="auto", tensor_parallel_size=1, gp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355 bug;rocm ### Your current environment ### 🐛 Describe the bug On ROCm `gfx950` / MI355, `fxmarty/qwen_1.5-moe-a2.7b-mxfp4` loads...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355 bug;rocm ### Your current environment ### 🐛 Describe the bug On ROCm `gfx950` / MI355, `fxmarty/qwen_1.5-moe-a2.7b-mxfp4` lo
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355 bug;rocm ### Your current environment ### 🐛 Describe the bug On ROCm `gfx950` / MI355, `fxmarty/qwen_1.5-moe-a2.7b-mxfp4` loads...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [ROCm][Bug]: Quark MXFP4 `w_mxfp4_a_mxfp4` linear path corrupts Qwen1.5-MoE output on MI355 bug;rocm ### Your current environment ### 🐛 Describe the bug On ROCm `gfx950` / MI355, `fxmarty/qwen_1.5-moe-a2.7b-mxfp4` loads...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
