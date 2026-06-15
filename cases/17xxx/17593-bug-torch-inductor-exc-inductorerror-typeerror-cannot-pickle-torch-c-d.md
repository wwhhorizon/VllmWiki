# vllm-project/vllm#17593: [Bug]: torch._inductor.exc.InductorError: TypeError: cannot pickle 'torch._C.DispatchKeySet' object

| 字段 | 值 |
| --- | --- |
| Issue | [#17593](https://github.com/vllm-project/vllm/issues/17593) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch._inductor.exc.InductorError: TypeError: cannot pickle 'torch._C.DispatchKeySet' object

### Issue 正文摘录

### Your current environment vLLM main branch, PyTorch main branch ### 🐛 Describe the bug Repro: `pytest -v -s tests/compile/piecewise/test_toy_llama.py` Gives: ``` > rv = reductor(4) E torch._inductor.exc.InductorError: TypeError: cannot pickle 'torch._C.DispatchKeySet' object E E Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even m ore developer context, set TORCH_LOGS="+dynamo" ../env/lib/python3.12/copy.py:151: InductorError ====================================================================== warnings summary ======================================================================= ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ror: TypeError: cannot pickle 'torch._C.DispatchKeySet' object bug;torch.compile;stale ### Your current environment vLLM main branch, PyTorch main branch ### 🐛 Describe the bug Repro: `pytest -v -s tests/compile/piecewi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ]: torch._inductor.exc.InductorError: TypeError: cannot pickle 'torch._C.DispatchKeySet' object bug;torch.compile;stale ### Your current environment vLLM main branch, PyTorch main branch ### 🐛 Describe the bug Repro: `p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Describe the bug Repro: `pytest -v -s tests/compile/piecewise/test_toy_llama.py` Gives: ``` > rv = reductor(4) E torch._inductor.exc.InductorError: TypeError: cannot pickle 'torch._C.DispatchKeySet' object E E Se
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eError: cannot pickle 'torch._C.DispatchKeySet' object bug;torch.compile;stale ### Your current environment vLLM main branch, PyTorch main branch ### 🐛 Describe the bug Repro: `pytest -v -s tests/compile/piecewise/test_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
