# vllm-project/vllm#1200: Key Error when handle multiple requests simultaneously

| 字段 | 值 |
| --- | --- |
| Issue | [#1200](https://github.com/vllm-project/vllm/issues/1200) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Key Error when handle multiple requests simultaneously

### Issue 正文摘录

There was a previous thread but I didnt see a resolution, running into this issue: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: 30 CPU RAM: 200 GPU: 8, Tesla V100-SXM2 ``` vllm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=1) summary_prompt = """ Summarize the message below, delimited by triple backticks, using short bullet points. ```{message}``` BULLET POINT SUMMARY: """ generated_summary = summarize( vllm, summary_prompt, sampling_params) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 130, in generate return self._run_engine(use_tqdm) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/llm.py", line 150, in _run_engine step_outputs = self.llm_engine.step() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 559, in step return self._process_model_outputs(output, scheduler_outputs) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 518, in _process_model_outputs self._process_sequence_group_samples(seq_group, samples) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 357, in _process_sequence_group_samples paren...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Key Error when handle multiple requests simultaneously bug;stale There was a previous thread but I didnt see a resolution, running into this issue: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: 30 CPU RAM: 200 GPU: 8, Tesla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: didnt see a resolution, running into this issue: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: 30 CPU RAM: 200 GPU: 8, Tesla V100-SXM2 ``` vllm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ``` vllm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=1) summary_prompt = """ Summarize the message below, delimited by triple backticks, using short bullet points....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut I didnt see a resolution, running into this issue: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: 30 CPU RAM: 200 GPU: 8, Tesla V100-SXM2 ``` vllm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rsion: 11.2 CPU: 30 CPU RAM: 200 GPU: 8, Tesla V100-SXM2 ``` vllm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=1) summary_prompt = """ Summarize the message below,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
