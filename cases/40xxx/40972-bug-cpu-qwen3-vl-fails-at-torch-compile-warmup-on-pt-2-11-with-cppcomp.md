# vllm-project/vllm#40972: [Bug]: [CPU] Qwen3-VL fails at torch.compile warmup on PT 2.11 with CppCompileError: VecMask<...>::VecMask(int&)

| 字段 | 值 |
| --- | --- |
| Issue | [#40972](https://github.com/vllm-project/vllm/issues/40972) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [CPU] Qwen3-VL fails at torch.compile warmup on PT 2.11 with CppCompileError: VecMask<...>::VecMask(int&)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On PyTorch 2.11, running any Qwen3-VL model on the vLLM CPU backend fails during `torch.compile` C++ codegen with: ``` torch._inductor.exc.InductorError: CppCompileError: ... compilation terminated ... no matching function for call to 'at::vec::CPU_CAPABILITY::VecMask ::VecMask(int&)' ``` The crash happens in the warmup compile step, so the engine never finishes initialization and no tokens are ever generated. Qwen3 text-only models such as Qwen3-4B do not exercise this code path and run fine on the same build. ### Root cause Inductor's `CppVecKernel.indirect_assert` builds the mask string for tail-vectorized loops like this: ```python mask = f"{self._get_mask_type(var.dtype)}({mask})" ``` When `mask` is a scalar (which is what indirect indexing inside the tail of a vectorized loop produces), the resulting C++ looks like `VecMask (scalar_int)`. `VecMask` does not have an `(int)` constructor; the right call site is `VecMask ::from(scalar)`, which the type provides specifically for this conversion. g++ then fails to find an overload and the whole compile aborts. ### Reproduction **Minimal PyTorch repro** (mirrors the regression tes...

## 现有链接修复摘要

#40973 [Bugfix][CPU] Backport PT cpp codegen indirect_assert scalar-mask fix

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: [CPU] Qwen3-VL fails at torch.compile warmup on PT 2.11 with CppCompileError: VecMask<...>::VecMask(int&) bug ### Your current environment ### 🐛 Describe the bug On PyTorch 2.11, running any Qwen3-VL model on the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ompilation terminated ... no matching function for call to 'at::vec::CPU_CAPABILITY::VecMask ::VecMask(int&)' ``` The crash happens in the warmup compile step, so the engine never finishes initialization and no tokens a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [CPU] Qwen3-VL fails at torch.compile warmup on PT 2.11 with CppCompileError: VecMask<...>::VecMask(int&) bug ### Your current environment ### 🐛 Describe the bug On PyTorch 2.11, running any Qwen3-VL model on the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ibe the bug On PyTorch 2.11, running any Qwen3-VL model on the vLLM CPU backend fails during `torch.compile` C++ codegen with: ``` torch._inductor.exc.InductorError: CppCompileError: ... compilation terminated ... no ma...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: tual = torch.compile(fn, fullgraph=True)(positions, cache) torch.testing.assert_close(actual, expected) ``` Output on PT 2.11.0+cpu: ``` torch._inductor.exc.InductorError: CppCompileError: C++ compile error ...main.cpp:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40973](https://github.com/vllm-project/vllm/pull/40973) | closes_keyword | 0.95 | [Bugfix][CPU] Backport PT cpp codegen indirect_assert scalar-mask fix | Fixes #40972 This blocks running every Qwen3-VL size on vLLM CPU on torch 2.11. Qwen3 text-only models (e.g. Qwen3-4B) do not hit the path and are unaffected. Upstream fix i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
