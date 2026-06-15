# vllm-project/vllm#25352: [Bug]: AssertionError while passing otlp_traces_endpoint in Mac

| 字段 | 值 |
| --- | --- |
| Issue | [#25352](https://github.com/vllm-project/vllm/issues/25352) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError while passing otlp_traces_endpoint in Mac

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running the code below, just a basic setup, but I am facing this error, I've done the setup from source as described here - https://docs.vllm.ai/en/v0.9.2/getting_started/installation/cpu.html#pre-built-wheels Following this to setup opentelemetry - https://docs.vllm.ai/en/latest/examples/online_serving/opentelemetry.html ``` Traceback (most recent call last): File "/Users/shashank/Desktop/sks/vllm-work/inf.py", line 14, in outputs = llm.generate(prompts, sampling_params) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/shashank/Desktop/sks/vllm-work/vllmenv/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 404, in generate outputs = self._run_engine(use_tqdm=use_tqdm) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/shashank/Desktop/sks/vllm-work/vllmenv/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 1603, in _run_engine step_outputs = self.llm_engine.step() ^^^^^^^^^^^^^^^^^^^^^^ File "/Users/shashank/Desktop/sks/vllm-work/vllmenv/lib/python3.11/site-packages/vllm/v1/engine/llm_engine.py", line 252, in step processed_outputs = self.output_processor.process_outputs( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ibe the bug I am running the code below, just a basic setup, but I am facing this error, I've done the setup from source as described here - https://docs.vllm.ai/en/v0.9.2/getting_started/installation/cpu.html#pre-built...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m", otlp_traces_endpoint="http://localhost:4317") outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: AssertionError while passing otlp_traces_endpoint in Mac bug;stale ### Your current environment ### 🐛 Describe the bug I am running the code below, just a basic setup, but I am facing this error, I've done the se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: heels Following this to setup opentelemetry - https://docs.vllm.ai/en/latest/examples/online_serving/opentelemetry.html ``` Traceback (most recent call last): File "/Users/shashank/Desktop/sks/vllm-work/inf.py", line 14...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
