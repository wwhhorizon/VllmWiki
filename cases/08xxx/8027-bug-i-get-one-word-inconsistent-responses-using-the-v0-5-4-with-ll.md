# vllm-project/vllm#8027: [Bug]: I get one word inconsistent responses using the v0.5.4 with LL

| 字段 | 值 |
| --- | --- |
| Issue | [#8027](https://github.com/vllm-project/vllm/issues/8027) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: I get one word inconsistent responses using the v0.5.4 with LL

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed the vllm server using below ``` model_dir = _model_file APP_PORT = os.getenv("APP_PORT", "8002") command = [ '/opt/venv/bin/python3', '-m', 'vllm.entrypoints.openai.api_server', '--model', model_dir, '--host', '0.0.0.0', '--port', APP_PORT, '--gpu-memory-utilization', '0.75', '--max-model-len', '4096', '--max-num-seqs', '512', '--served-model-name', model_name, '--chat-template', '/app/artifacts/llama_template.jinja' ] subprocess.run(command) ``` and used a class to call the API for both client.completion.create and client.chat.completion.create in which I get one word and garbage responses such as "success", "okay", "2110" and so on. ``` prompts = [ "\n{system_message} \n{prompt} \n\n".format(system_message=PROMPT, prompt=text) ] request = {"model_name": "Meta-Llama-3-8B-Instruct", "prompt": prompts, "max_tokens": 3072, "temperature": 0.8, "grammar": grammar } res = VllmClient().open_ai_vllm(request) res.choices[0].text ``` with below result, I get coherent responses sometimes though {"result": "2100.0"} ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug I deployed the vllm server using below ``` model_dir = _model_file APP_PORT = os.getenv("APP_PORT", "8002") command = [ '/opt/venv/bin/python3', '-m', 'vllm.entrypoints.openai.api_server', '--mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: I get one word inconsistent responses using the v0.5.4 with LL bug;stale ### Your current environment ### 🐛 Describe the bug I deployed the vllm server using below ``` model_dir = _model_file APP_PORT = os.getenv(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0"} ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
