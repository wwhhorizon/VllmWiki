# vllm-project/vllm#17931: invalid conversion from ‘int’ to ‘CUresult’ {aka ‘cudaError_enum’}

| 字段 | 值 |
| --- | --- |
| Issue | [#17931](https://github.com/vllm-project/vllm/issues/17931) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> invalid conversion from ‘int’ to ‘CUresult’ {aka ‘cudaError_enum’}

### Issue 正文摘录

### Your current environment ‘DevicePtrInfo getPointer(PyObject*, int)’: /tmp/tmpp8zry39f/main.c:118:20: error: invalid conversion from ‘int’ to ‘CUresult’ {aka ‘cudaError_enum’} [-fpermissive] 118 | CUDA_CHECK(status); // Catch any other cuda API errors | ^ | | | int /tmp/tmpp8zry39f/main.c:24:38: note: in definition of macro ‘CUDA_CHECK’ 24 | #define CUDA_CHECK(ans) { gpuAssert((ans), __FILE__, __LINE__); } | ^~~ /tmp/tmpp8zry39f/main.c:7:39: note: initializing argument 1 of ‘void gpuAssert(CUresult, const char*, int)’ 7 | static inline void gpuAssert(CUresult code, const char *file, int line) | ~~~~~~~~~^~~~ ERROR 05-10 09:24:36 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 05-10 09:24:36 [core.py:387] File "/home/house365ai/anaconda3/envs/vllm6/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 05-10 09:24:36 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-10 09:24:36 [core.py:387] File "/home/house365ai/anaconda3/envs/vllm6/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 320, in __init__ ERROR 05-10 09:24:36 [core.py:387] super().__init__(vllm_config, executor_class, lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: invalid conversion from ‘int’ to ‘CUresult’ {aka ‘cudaError_enum’} installation;stale ### Your current environment ‘DevicePtrInfo getPointer(PyObject*, int)’: /tmp/tmpp8zry39f/main.c:118:20: error: invalid conversion fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: in __init__ ERROR 05-10 09:24:36 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 05-10 09:24:36 [core.py:387] File "/home/house365ai/anaconda3/envs/vllm6/lib/python3.10/site-packages/vllm/v1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nvert.py", line 962, in step ERROR 05-10 09:24:36 [core.py:387] self.dispatch_table[inst.opcode](self, inst) ERROR 05-10 09:24:36 [core.py:387] File "/home/house365ai/anaconda3/envs/vllm6/lib/python3.10/site-packages/to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vailable_memory ERROR 05-10 09:24:36 [core.py:387] self.model_runner.profile_run() ERROR 05-10 09:24:36 [core.py:387] File "/home/house365ai/anaconda3/envs/vllm6/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: invalid conversion from ‘int’ to ‘CUresult’ {aka ‘cudaError_enum’} installation;stale ### Your current environment ‘DevicePtrInfo getPointer(PyObject*, int)’: /tmp/tmpp8zry39f/main.c:118:20: error: invalid conversion fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
