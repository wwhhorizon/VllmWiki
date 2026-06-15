# vllm-project/vllm#9234: [issue tracker] make quantization compatible with dynamo dynamic shape

| 字段 | 值 |
| --- | --- |
| Issue | [#9234](https://github.com/vllm-project/vllm/issues/9234) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [issue tracker] make quantization compatible with dynamo dynamic shape

### Issue 正文摘录

### Anything you want to discuss about vllm. here is a simple demo code: ```python import torch from torch.utils.cpp_extension import load_inline custom_library = torch.library.Library("custom", "DEF") custom_library.define("add_cpp(Tensor x, int y) -> Tensor") cpp_source = """ #include torch::Tensor custom_add(torch::Tensor x, int64_t y) { return x + y; } TORCH_LIBRARY_IMPL(custom, CPU, m) { m.impl("add_cpp", custom_add); } """ custom_op = load_inline( name="custom_op", cpp_sources=cpp_source, extra_cflags=[], functions=["custom_add"] ) @torch.library.register_fake("custom::add_cpp") def _(x: torch.Tensor, y: int) -> torch.Tensor: return torch.empty((y,), dtype=torch.float32) import torch @torch.library.custom_op("custom::add_py", mutates_args=[]) def add_py(x: torch.Tensor, y: int) -> torch.Tensor: return x + y @add_py.register_fake def _(x: torch.Tensor, y: int) -> torch.Tensor: return torch.empty((y,), dtype=torch.float32) @torch.compile(backend="eager", fullgraph=True) def f(x): # return torch.ops.custom.add_py(x, x.shape[0]) # passes return torch.ops.custom.add_cpp(x, x.shape[0]) # errors with `Not all values of RelaxedUnspecConstraint(L['x'].size()[0]) are valid because L['...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: you want to discuss about vllm. here is a simple demo code: ```python import torch from torch.utils.cpp_extension import load_inline custom_library = torch.library.Library("custom", "DEF") custom_library.define("add_cpp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [issue tracker] make quantization compatible with dynamo dynamic shape ### Anything you want to discuss about vllm. here is a simple demo code: ```python import torch from torch.utils.cpp_extension import load_inline cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ensor: return torch.empty((y,), dtype=torch.float32) @torch.compile(backend="eager", fullgraph=True) def f(x): # return torch.ops.custom.add_py(x, x.shape[0]) # passes return torch.ops.custom.add_cpp(x, x.shape[0]) # er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
