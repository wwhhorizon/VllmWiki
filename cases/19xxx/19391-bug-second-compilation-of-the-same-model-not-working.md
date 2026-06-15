# vllm-project/vllm#19391: [Bug]: Second compilation of the same model not working

| 字段 | 值 |
| --- | --- |
| Issue | [#19391](https://github.com/vllm-project/vllm/issues/19391) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Second compilation of the same model not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `CompilationLevel.DYNAMO_AS_IS` with a custom backend on the same model twice, that backend is only invoked by Dynamo the first time around. Disabling caching with `TORCHINDUCTOR_FX_GRAPH_CACHE=0` and `TORCHINDUCTOR_FORCE_DISABLE_CACHES=0` does not help. I get there are cases where this is intended behavior, but maybe the custom `backend` changes between invocations and we want to recompile (the case in a unit test I'm writing). Is there a separate cache I'm missing? ```python from copy import deepcopy from torch import fx from vllm import LLM, SamplingParams from vllm.config import CompilationConfig, CompilationLevel def backend(graph: fx.GraphModule, example_inputs): print("Backend called!") from torch._inductor.compile_fx import compile_fx return compile_fx(graph, example_inputs) model = "redhatai/Meta-Llama-3.1-8B-Instruct-FP8" if __name__ == '__main__': sampling_params = SamplingParams(temperature=0.0, max_tokens=10, top_p=0.95) compile_config = CompilationConfig( # DYNAMO_AS_IS triggers custom backend & does full Dynamo compilation level=CompilationLevel.DYNAMO_AS_IS, backend="__main__.backend", ) # Prints "Backe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: maybe the custom `backend` changes between invocations and we want to recompile (the case in a unit test I'm writing). Is there a separate cache I'm missing? ```python from copy import deepcopy from torch import fx from...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _fx(graph, example_inputs) model = "redhatai/Meta-Llama-3.1-8B-Instruct-FP8" if __name__ == '__main__': sampling_params = SamplingParams(temperature=0.0, max_tokens=10, top_p=0.95) compile_config = Compilatio
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Second compilation of the same model not working bug ### Your current environment ### 🐛 Describe the bug When using `CompilationLevel.DYNAMO_AS_IS` with a custom backend on the same model twice, that backend is o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: scribe the bug When using `CompilationLevel.DYNAMO_AS_IS` with a custom backend on the same model twice, that backend is only invoked by Dynamo the first time around. Disabling caching with `TORCHINDUCTOR_FX_GRAPH_CACHE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
