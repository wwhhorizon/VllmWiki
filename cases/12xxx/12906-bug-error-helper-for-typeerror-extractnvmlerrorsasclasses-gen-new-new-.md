# vllm-project/vllm#12906: [Bug]: error helper for TypeError: _extractNVMLErrorsAsClasses..gen_new..new() takes 1 positional argument but 2 were given

| 字段 | 值 |
| --- | --- |
| Issue | [#12906](https://github.com/vllm-project/vllm/issues/12906) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error helper for TypeError: _extractNVMLErrorsAsClasses..gen_new..new() takes 1 positional argument but 2 were given

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug If anyone encountered this error, this issue helps track the problem. the root cause is a bug in https://pypi.org/project/nvidia-ml-py , that its dynamically created exception class cannot be deserialized. a minimal reproducible example: ```python # pip install -U nvidia-ml-py import pynvml import pickle error_data = None try: pynvml.nvmlInit() pynvml.nvmlDeviceGetHandleByIndex(1000) except Exception as e: data = pickle.dumps(e) error_data = data # error here # TypeError: _extractNVMLErrorsAsClasses. .gen_new. .new() takes 1 positional argument but 2 were given print(pickle.loads(data)) ``` the fact that the exception cannot be deserialized, becomes worse when it is used together with `ray`, because `ray` will try to deserialize the error in the driver process: ```python def f(): import pynvml pynvml.nvmlInit() pynvml.nvmlDeviceGetHandleByIndex(1000) # call it directly, we can get clear error message # NVMLError_InvalidArgument: Invalid Argument f() import ray ray.init() # call it in ray, we cannot get clear error message. # the error will be # RuntimeError: Failed to unpickle serialized exception # TypeError: _extractNVMLEr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ically created exception class cannot be deserialized. a minimal reproducible example: ```python # pip install -U nvidia-ml-py import pynvml import pickle error_data = None try: pynvml.nvmlInit() pynvml.nvmlDeviceGetHan...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s dynamically created exception class cannot be deserialized. a minimal reproducible example: ```python # pip install -U nvidia-ml-py import pynvml import pickle error_data = None try: pynvml.nvmlInit() pynvml.nvmlDevic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Classes..gen_new..new() takes 1 positional argument but 2 were given bug;stale ### Your current environment None ### 🐛 Describe the bug If anyone encountered this error, this issue helps track the problem. the root caus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
