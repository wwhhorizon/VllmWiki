# vllm-project/vllm#7327: [Bug]: Endless generation with fine tuned llama 3.1 model 

| 字段 | 值 |
| --- | --- |
| Issue | [#7327](https://github.com/vllm-project/vllm/issues/7327) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Endless generation with fine tuned llama 3.1 model 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have deployed a fine tuned version of llama 3.1 for inference on my server using this command: sudo docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -v ./chat_templates/template_llama_3_1.jinja:/template_llama_3_1.jinja --env "HUGGING_FACE_HUB_TOKEN=hf_..By" -p 8000:8000 --ipc=host docker.io/vllm/vllm-openai:v0.5.3.post1 --model shreshtbsc/llama3.1-ft --max_model_len=8000 --chat-template "/template_llama_3_1.jinja" It has been deployed successfully but when I send requests to the server using the openai client like this: response = client.chat.completions.create( model=CHATBOT_MODEL_NAME, messages=messages, max_tokens=200, extra_body={"stop_token_ids": [128001,128008,128009]} ) I get endless generation in my responses even though I have passed the max_tokens and stop_token_id parameter. Upon further investigation in the logs of my server, I noticed that the max_tokens and stop_token_id parameter are not being received. These are the logs I receive: params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, see...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ent environment ### 🐛 Describe the bug I have deployed a fine tuned version of llama 3.1 for inference on my server using this command: sudo docker run --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -v ./ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Endless generation with fine tuned llama 3.1 model bug;stale ### Your current environment ### 🐛 Describe the bug I have deployed a fine tuned version of llama 3.1 for inference on my server using this command: su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Endless generation with fine tuned llama 3.1 model bug;stale ### Your current environment ### 🐛 Describe the bug I have deployed a fine tuned version of llama 3.1 for inference on my server using this command: su...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
