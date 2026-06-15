# vllm-project/vllm#14392: [Bug]: Enable lora returns garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#14392](https://github.com/vllm-project/vllm/issues/14392) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enable lora returns garbage output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We got garbage output when serving with `--enable-lora` and `--max-loras 2`. ``` vllm serve unsloth/Llama-3.2-1B \ --tensor-parallel-size 4 \ --enable-lora \ --max-loras 2 \ --dtype float16 \ --max-model-len 6000 ``` Then serve the base model: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "unsloth/Llama-3.2-1B", "prompt": "San Francisco is a", "max_tokens": 256, "temperature": 0.9 }' ``` Got garbage output: ``` {"id":"cmpl-bcfe6fb77b114935b2c6ff033008ea83","object":"text_completion","created":1741310698,"model":"unsloth/Llama-3.2-1B","choices":[{"index":0,"text":" city of(GUIраницa 6раницyраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницaраницa Hokue(GUIраницaTumblr) is a GREEN(GUI meetup) in(GUI_Base) and it(GUI(GUIраницa(GUI meetup)))(GUITumblr))(GUI meetup Prozent(GUI conformsTumblr conforms conforms conforms conforms conforms conforms conforms conforms conforms parenthesis conforms parenthesis parenthesis Nearby Holding rooms Near reacted No No No No No No No No No No No No No No No No No Norfuge No No No No No Norfuge Hotel (...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d '{ "model": "unsloth/Llama-3.2-1B", "prompt": "San Francisco is a", "max_tokens": 256, "temperature": 0.9 }' ``` Got garbage output: ``` {"id":"cmpl-bcfe6fb77b114935b2c6ff033008ea83","object":"text_completion","create...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: --tensor-parallel-size 4 \ --enable-lora \ --max-loras 2 \ --dtype float16 \ --max-model-len 6000 ``` Then serve the base model: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: erving with `--enable-lora` and `--max-loras 2`. ``` vllm serve unsloth/Llama-3.2-1B \ --tensor-parallel-size 4 \ --enable-lora \ --max-loras 2 \ --dtype float16 \ --max-model-len 6000 ``` Then serve the base model: ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Enable lora returns garbage output bug;stale ### Your current environment ### 🐛 Describe the bug We got garbage output when serving with `--enable-lora` and `--max-loras 2`. ``` vllm serve unsloth/Llama-3.2-1B \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
