# vllm-project/vllm#35293: [Bug] GLM-5-FP8 Crash: CUDAGraph Replay Segmentation Fault

| 字段 | 值 |
| --- | --- |
| Issue | [#35293](https://github.com/vllm-project/vllm/issues/35293) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;operator |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] GLM-5-FP8 Crash: CUDAGraph Replay Segmentation Fault

### Issue 正文摘录

### Your current environment 8*H200 ```text vLLM version：0.16.0rc2.dev123+gec12d39d4 + GLM5-FP8 ``` ```Bash vllm serve /path/to/GLM-5-FP8 \ --served-model-name GLM5 \ --tensor-parallel-size 8 \ --dtype auto \ --gpu-memory-utilization 0.90 \ --max-model-len 200000 \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --reasoning-parser glm45 ``` ### 🐛 Describe the bug !!!!!!! Segfault encountered !!!!!!! File " ", line 0, in cuGraphLaunch File " ", line 0, in cudaGraphLaunch File " ", line 0, in at::cuda::CUDAGraph::replay() File " ", line 0, in torch::detail::wrap_pybind_function_impl_ (void (at::cuda::CUDAGraph::*&&)(), std::integer_sequence , std::integral_constant )::{lambda(at::cuda::CUDAGraph&)#1}::operator()(at::cuda::CUDAGraph&) const File " ", line 0, in pybind11::cpp_function::initialize (void (at::cuda::CUDAGraph::*&&)(), std::integer_sequence , std::integral_constant )::{lambda(at::cuda::CUDAGraph&)#1}, void, at::cuda::CUDAGraph&, pybind11::name, pybind11::is_method, pybind11::sibling>(void (at::cuda::CUDAGraph::*&&)(), void (*)(at::cuda::CUDAGraph&), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&)::{lambda(pybind11:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug] GLM-5-FP8 Crash: CUDAGraph Replay Segmentation Fault bug ### Your current environment 8*H200 ```text vLLM version：0.16.0rc2.dev123+gec12d39d4 + GLM5-FP8 ``` ```Bash vllm serve /path/to/GLM-5-FP8 \ --served-model-n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Segmentation Fault bug ### Your current environment 8*H200 ```text vLLM version：0.16.0rc2.dev123+gec12d39d4 + GLM5-FP8 ``` ```Bash vllm serve /path/to/GLM-5-FP8 \ --served-model-name GLM5 \ --tensor-parallel-size 8 \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug] GLM-5-FP8 Crash: CUDAGraph Replay Segmentation Fault bug ### Your current environment 8*H200 ```text vLLM version：0.16.0rc2.dev123+gec12d39d4 + GLM5-FP8 ``` ```Bash vllm serve /path/to/GLM-5-FP8 \ --served-model-n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ::detail::function_call&) File " ", line 0, in pybind11::cpp_function::dispatcher(_object*, _object*, _object*) File " ", line 0, in _PyObject_MakeTpCall File " ", line 0, in _PyEval_EvalFrameDefault File " ", line 0, i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 2d39d4 + GLM5-FP8 ``` ```Bash vllm serve /path/to/GLM-5-FP8 \ --served-model-name GLM5 \ --tensor-parallel-size 8 \ --dtype auto \ --gpu-memory-utilization 0.90 \ --max-model-len 200000 \ --trust-remote-code \ --enable-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
