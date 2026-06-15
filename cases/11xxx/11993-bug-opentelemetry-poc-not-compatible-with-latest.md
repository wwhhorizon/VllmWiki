# vllm-project/vllm#11993: [Bug]: opentelemetry POC not compatible with latest

| 字段 | 值 |
| --- | --- |
| Issue | [#11993](https://github.com/vllm-project/vllm/issues/11993) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: opentelemetry POC not compatible with latest

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to install this with latest opentelemetry, specifically I add otel requirements with EDOT bootstrap instead of the older versions in the POC https://docs.vllm.ai/en/latest/getting_started/examples/opentelemetry.html ``` pip install elastic-opentelemetry edot-bootstrap >> otel-requirements.txt pip install -r otel-requirements.txt ``` When I run with opentelemetry-instrument, things are ok, just I am missing the span this project creates ``` dotenv run -- opentelemetry-instrument vllm serve Qwen/Qwen2.5-0.5B ``` To get the span (since our instrumentation isn't configured as an entrypoint..), I need to add an arg. If I do, it crashes like this ```bash $ dotenv run -- opentelemetry-instrument vllm serve Qwen/Qwen2.5-0.5B --otlp-traces-endpoint=http://localhost:4318/v1/traces --snip-- ERROR 01-13 15:42:51 engine.py:387] ModuleNotFoundError: No module named 'opentelemetry.semconv_ai' ERROR 01-13 15:42:51 engine.py:387] Process SpawnProcess-1: Traceback (most recent call last): File "/Users/adriancole/.pyenv/versions/3.12.8/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to install this with latest opentelemetry, specifically I add otel requirements with EDOT bootstrap instead of the older versions in the POC https://doc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: POC not compatible with latest bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to install this with latest opentelemetry, specifically I add otel requirements with EDO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 513 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: opentelemetry POC not compatible with latest bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to install this with latest opentelemetry, specifically I add otel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
