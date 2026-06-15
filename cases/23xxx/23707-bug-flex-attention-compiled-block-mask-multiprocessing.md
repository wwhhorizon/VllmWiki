# vllm-project/vllm#23707: [Bug]: Flex Attention compiled block mask + multiprocessing

| 字段 | 值 |
| --- | --- |
| Issue | [#23707](https://github.com/vllm-project/vllm/issues/23707) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Flex Attention compiled block mask + multiprocessing

### Issue 正文摘录

### Your current environment ## Summary ``` import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLEX_ATTENTION" # os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" from vllm import LLM, SamplingParams model = LLM("Qwen/Qwen2-7B-Instruct", enforce_eager=True, tensor_parallel_size=1) output = model.generate(["Hi"] * 4) print(output) ``` The :5 ========= Host Frame: kernel_call in triton_heuristics.py:789 ========= Host Frame: benchmark_gpu in benchmarking.py:243 ========= Host Frame: wrapper in benchmarking.py:39 ========= Host Frame: bench in triton_heuristics.py:804 ========= Host Frame: benchmark_all_configs in triton_heuristics.py:935 ========= Host Frame: autotune_to_one_config in triton_heuristics.py:960 ========= Host Frame: run in triton_heuristics.py:1133 ========= Host Frame: call in cxjfwhfthdys3542oejiosmoznjm67tdzfqrokftdhz6z25pxepc.py:617 ========= Host Frame: run in utils.py:2716 ========= Host Frame: __call__ in output_code.py:584 ========= Host Frame: wrapper in runtime_wrappers.py:556 ========= Host Frame: inner_fn in runtime_wrappers.py:750 ========= Host Frame: call_func_at_runtime_with_args in utils.py:126 ========= Host Frame: runtime_wrapper in runtime_wrappers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Flex Attention compiled block mask + multiprocessing bug;stale ### Your current environment ## Summary ``` import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLEX_ATTENTION" # os.environ["VLLM_ENABLE_V1_MULTIPROCE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: M_ENABLE_V1_MULTIPROCESSING"] = "0" from vllm import LLM, SamplingParams model = LLM("Qwen/Qwen2-7B-Instruct", enforce_eager=True, tensor_parallel_size=1) output = model.generate(["Hi"] * 4) print(output) ``` The :5 ===...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e: kernel_call in triton_heuristics.py:789 ========= Host Frame: benchmark_gpu in benchmarking.py:243 ========= Host Frame: wrapper in benchmarking.py:39 ========= Host Frame: bench in triton_heuristics.py:804 =========...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: urrent environment ## Summary ``` import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLEX_ATTENTION" # os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" from vllm import LLM, SamplingParams model = LLM("Qwen/Qwen2-7B-In...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stics.py:1133 ========= Host Frame: call in cxjfwhfthdys3542oejiosmoznjm67tdzfqrokftdhz6z25pxepc.py:617 ========= Host Frame: run in utils.py:2716 ========= Host Frame: __call__ in output_code.py:584 ========= Host Fram...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
