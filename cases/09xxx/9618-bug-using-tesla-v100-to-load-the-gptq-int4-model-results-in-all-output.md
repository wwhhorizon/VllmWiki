# vllm-project/vllm#9618: [Bug]: "Using Tesla V100 to load the GPTQ-Int4 model results in all output being exclamation marks."

| 字段 | 值 |
| --- | --- |
| Issue | [#9618](https://github.com/vllm-project/vllm/issues/9618) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "Using Tesla V100 to load the GPTQ-Int4 model results in all output being exclamation marks."

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` messages = [{"role": "system", "content": "You are an helpful assistant."}] def chat_with_model(user_input): messages.append({"role": "user", "content": user_input}) response = client.chat.completions.create( model=model_name, messages=messages, temperature=0.7, top_p=0.8, # max_tokens=1024, extra_body={ "repetition_penalty": 1.05 }, stream=True, ) # 收集回复 full_reply = "" for chunk in response: content = chunk.choices[0].delta.content or "" print(content, end="", flush=True) full_reply += content print() messages.append({"role": "assistant", "content": full_reply}) def save_session(): """保存当前会话到JSON文件""" timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") filename = f"message_{timestamp}.json" with open(filename, 'w', encoding='utf-8') as f: json.dump(messages, f, ensure_ascii=False, indent=4) print(f"会话已保存到 {filename}") def main(): while True: user_input = [] print("User：", end="") # 处理多行输入 line = input() while not line.endswith("\\"): user_input.append(line) line = input() user_input.append(line[:-1]) # 去掉最后一个反斜杠 # 组装完整输入 complete_input = "\n".join(user_input) if complete_input.lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: me, 'w', encoding='utf-8') as f: json.dump(messages, f, ensure_ascii=False, indent=4) print(f"会话已保存到 {filename}") def main(): while True: user_input = [] print("User：", end="") # 处理多行输入 line = input() while not line.end...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: "Using Tesla V100 to load the GPTQ-Int4 model results in all output being exclamation marks." bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` messages = [{"ro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: "Using Tesla V100 to load the GPTQ-Int4 model results in all output being exclamation marks." bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` messages = [{"ro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the GPTQ-Int4 model results in all output being exclamation marks." bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` messages = [{"role": "system", "content": "You ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
