# vllm-project/vllm#14753: [Feature]: Support Gemma3 GGUF

| 字段 | 值 |
| --- | --- |
| Issue | [#14753](https://github.com/vllm-project/vllm/issues/14753) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Gemma3 GGUF

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Need support Gemma3 GGUF I also tried to try Gema 3 GGUF (https://huggingface.co/bartowski/google_gemma-3-27b-it-GGUF). An hour ago I downloaded the latest vllm code, built everything from sources. Including the latest version of transformers: pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 Here is the error when starting: File "/home/hackey/miniconda3/envs/python312/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/hackey/miniconda3/envs/python312/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/hackey/AI/vllm/vllm/engine/multiprocessing/engine.py", line 413, in run_mp_engine raise e File "/home/hackey/AI/vllm/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/hackey/AI/vllm/vllm/engine/multiprocessing/engine.py", line 120, in from_engine_args engine_config = engine_args.create_engine_config(usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support Gemma3 GGUF feature request;stale ### 🚀 The feature, motivation and pitch Need support Gemma3 GGUF I also tried to try Gema 3 GGUF (https://huggingface.co/bartowski/google_gemma-3-27b-it-GGUF). An hou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: he latest vllm code, built everything from sources. Including the latest version of transformers: pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 Here is the error when starting: File "/home/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Gemma3 GGUF feature request;stale ### 🚀 The feature, motivation and pitch Need support Gemma3 GGUF I also tried to try Gema 3 GGUF (https://huggingface.co/bartowski/google_gemma-3-27b-it-GGUF). An hou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: line 399, in load_gguf_checkpoint raise ValueError(f"GGUF model with architecture {architecture} is not supported yet.") ValueError: GGUF model with architecture gemma3 is not supported yet.``` ### Alternatives _No resp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: onfig_dict = load_gguf_checkpoint(resolved_config_file, return_tensors=False)["config"] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/hackey/AI/vllm/venv/lib/python3.12/site-packages/trans...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
