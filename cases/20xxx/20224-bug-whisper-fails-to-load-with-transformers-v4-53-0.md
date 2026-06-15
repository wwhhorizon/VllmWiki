# vllm-project/vllm#20224: [Bug]: Whisper fails to load with transformers v4.53.0

| 字段 | 值 |
| --- | --- |
| Issue | [#20224](https://github.com/vllm-project/vllm/issues/20224) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Whisper fails to load with transformers v4.53.0

### Issue 正文摘录

### Your current environment vllm main @ 7b1895e6ce4942091e16da790af8c12772a1d384 ### 🐛 Describe the bug ``` vllm serve openai/whisper-large-v3 ``` This started failing once `transformers` v4.53.0 was released. ``` Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/rbryant/vllm/vllm/engine/multiprocessing/engine.py", line 460, in run_mp_engine raise e from None File "/home/rbryant/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine engine = MQLLMEngine.from_vllm_config( File "/home/rbryant/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config return cls( File "/home/rbryant/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__ self.engine = LLMEngine(*args, **kwargs) File "/home/rbryant/vllm/vllm/engine/llm_engine.py", line 268, in __init__ self._initialize_kv_caches() File "/home/rbryant/vllm/vllm/engine/llm_engine.py", line 413, in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/home/rbryant/vllm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ngine.py", line 446, in run_mp_engine engine = MQLLMEngine.from_vllm_config( File "/home/rbryant/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config return cls( File "/home/rbryant/vllm/vllm/engin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/home/rbryant/vllm/vllm/executor/executor_base.py", line 104, in determine_num_available_blocks results = self.collective_rpc("determi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 256, in determine_num_available_blocks self.model_runner.profile_run() File "/home/rbryant/vllm/venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: timodal/registry.py", line 281, in create_processor return factories.build_processor(ctx, cache=cache) File "/home/rbryant/vllm/vllm/multimodal/registry.py", line 88, in build_processor return self.processor(info, dummy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
