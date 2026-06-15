# vllm-project/vllm#18718: [Bug]: LLaMA 4 model loading fails with KeyError on missing parameter 'layers.10.feed_forward.experts.0.activation_fn.scales'

| 字段 | 值 |
| --- | --- |
| Issue | [#18718](https://github.com/vllm-project/vllm/issues/18718) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLaMA 4 model loading fails with KeyError on missing parameter 'layers.10.feed_forward.experts.0.activation_fn.scales'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to load a LLaMA 4 model (specifically [kishizaki-sci/Llama-4-Scout-17B-16E-Instruct-AWQ](https://huggingface.co/kishizaki-sci/Llama-4-Scout-17B-16E-Instruct-AWQ)) using vLLM results in a failure with a KeyError when loading weights. The traceback ends with: ``` self._engine = AsyncLLMEngine.from_engine_args(engine_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 684, in from_engine_args return async_engine_cls.from_vllm_config( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 657, in from_vllm_config return cls( ^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 612, in __init__ self.engine = self._engine_class(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 267, in __init__ super().__init__(*args, **kwargs) File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 275, in __i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: LLaMA 4 model loading fails with KeyError on missing parameter 'layers.10.feed_forward.experts.0.activation_fn.scales' bug;stale ### Your current environment ### 🐛 Describe the bug Trying to load a LLaMA 4 model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vironment ### 🐛 Describe the bug Trying to load a LLaMA 4 model (specifically [kishizaki-sci/Llama-4-Scout-17B-16E-Instruct-AWQ](https://huggingface.co/kishizaki-sci/Llama-4-Scout-17B-16E-Instruct-AWQ)) using vLLM resul...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ror on missing parameter 'layers.10.feed_forward.experts.0.activation_fn.scales' bug;stale ### Your current environment ### 🐛 Describe the bug Trying to load a LLaMA 4 model (specifically [kishizaki-sci/Llama-4-Scout-17...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: loading fails with KeyError on missing parameter 'layers.10.feed_forward.experts.0.activation_fn.scales' bug;stale ### Your current environment ### 🐛 Describe the bug Trying to load a LLaMA 4 model (specifically [kishiz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
