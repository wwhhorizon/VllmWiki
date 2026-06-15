# vllm-project/vllm#41645: [Bug]: gpt-oss MoE moe_forward fake-kernel shape mismatch breaks torch.compile + TP > 1 on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#41645](https://github.com/vllm-project/vllm/issues/41645) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;moe;quantization |
| 子分类 | edge_case |
| Operator 关键词 | cuda;kernel;moe;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss MoE moe_forward fake-kernel shape mismatch breaks torch.compile + TP > 1 on Blackwell

### Issue 正文摘录

### Summary `openai/gpt-oss-{20b,120b}` crash deterministically at first compiled forward on Blackwell with `tensor_parallel_size > 1`: ``` AssertionError: expected size 16384==16384, stride 2880==3072 at dim=0 Error in op: torch.ops.vllm.moe_forward.default buf10: assert_size_stride(buf10, (s72, 3072), (3072, 1), ...) ``` ### Repro ```python from vllm import LLM, SamplingParams def main(): llm = LLM("openai/gpt-oss-20b", tensor_parallel_size=2, quantization="mxfp4", gpu_memory_utilization=0.7, max_model_len=4096) print(llm.generate(["Hello, my name is"], SamplingParams(max_tokens=8))[0].outputs[0].text) if __name__ == "__main__": main() ``` Fails on v0.20.1 (and `main` HEAD) on B200 / GB200 / GB300 in ~45s. Passes on v0.20.0. ### Root cause `TrtLlmMxfp4Experts{Monolithic,Modular}` were changed by #40960 to allocate output at `hidden_dim_unpadded` (2880 for gpt-oss after MXFP4 256-alignment), while the registered fake kernel `_moe_forward_fake` (`vllm/model_executor/layers/fused_moe/runner/moe_runner.py`) still returns `torch.empty_like(hidden_states)` (3072). Inductor pre-bakes the 3072 stride; the runtime tensor is 2880-wide; the assert fires. Every other expert class (`TrtLlmNv...

## 现有链接修复摘要

#41646 [Bugfix] Restore moe_forward output shape invariant on TRTLLM MXFP4 path | #41931 [Bugfix] Fix MoE fake output shape for TRTLLM MXFP4

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: gpt-oss MoE moe_forward fake-kernel shape mismatch breaks torch.compile + TP > 1 on Blackwell ### Summary `openai/gpt-oss-{20b,120b}` crash deterministically at first compiled forward on Blackwell with `tensor_pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: gpt-oss MoE moe_forward fake-kernel shape mismatch breaks torch.compile + TP > 1 on Blackwell ### Summary `openai/gpt-oss-{20b,120b}` crash deterministically at first compiled forward on Blackwell with `tensor_pa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: llm = LLM("openai/gpt-oss-20b", tensor_parallel_size=2, quantization="mxfp4", gpu_memory_utilization=0.7, max_model_len=4096) print(llm.generate(["Hello, my name is"], SamplingParams(max_tokens=8))[0].outputs[0].text) i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ile + TP > 1 on Blackwell ### Summary `openai/gpt-oss-{20b,120b}` crash deterministically at first compiled forward on Blackwell with `tensor_parallel_size > 1`: ``` AssertionError: expected size 16384==16384, stride 28...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: sor_parallel_size > 1`: ``` AssertionError: expected size 16384==16384, stride 2880==3072 at dim=0 Error in op: torch.ops.vllm.moe_forward.default buf10: assert_size_stride(buf10, (s72, 3072), (3072, 1), ...) ``` ### Re...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41646](https://github.com/vllm-project/vllm/pull/41646) | closes_keyword | 0.95 | [Bugfix] Restore moe_forward output shape invariant on TRTLLM MXFP4 path | Fixes #41645. `gpt-oss-{20b,120b}` crashes under `torch.compile` with `tensor_parallel_size > 1` on Blackwell because of a fake/real shape mismatch in `vllm.moe_forward`: - The |
| [#41931](https://github.com/vllm-project/vllm/pull/41931) | closes_keyword | 0.95 | [Bugfix] Fix MoE fake output shape for TRTLLM MXFP4 | Fixes #41645. `vllm.moe_forward` and `vllm.moe_forward_shared` fake implementations always returned tensors with the same trailing dimension as `hidden_states`. The TRTLLM MXFP4 M |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
