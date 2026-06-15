# vllm-project/vllm#13100: [Usage]: Mistral Large crashes with concurrent long context requests

| 字段 | 值 |
| --- | --- |
| Issue | [#13100](https://github.com/vllm-project/vllm/issues/13100) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Mistral Large crashes with concurrent long context requests

### Issue 正文摘录

### Your current environment As I run vLLM in a docker container, I'll skip the `collect_env.py` step here. If you need the output of this in the docker container, I can run it there. I use the latest (0.7.2) vLLM image. The GPU is a A100 80GB. The docker compose script to start the container is below: I have the problem that I get "CUDA out of memory" crashes when calling multiple concurrent API requests with long questions. This only happens with Mistral Large (123B). The question is a long Lorem Ipsum text (4896 word), wich is ~10555 token according to https://token-counter.app/mistral/mistral-large. So this request should fit into the context of one query each. To test the behaviour of vLLM with concurrent requests, I have two scripts: - one wich sends the API call via curl - one which just calls the first script x times in parallel to simulate multiple users. I won't share the whole script, as there is alot of token/time calcultations, but the gist is below: req.sh: ```bash curl -X POST -H "Content-Type: application/json" http:// :3000/api/chat/completions \ -H 'Authorization: Bearer sk- ' \ -d "{\"model\": \"$model_name\", \"messages\":[{\"role\": \"user\", \"content\": \"$r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: /api/chat/completions \ -H 'Authorization: Bearer sk- ' \ -d "{\"model\": \"$model_name\", \"messages\":[{\"role\": \"user\", \"content\": \"$req_text\"}], \"stream\": true}" ``` concurr.sh: ```bash num_reqs=${1:-20} ec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: context requests usage ### Your current environment As I run vLLM in a docker container, I'll skip the `collect_env.py` step here. If you need the output of this in the docker container, I can run it there. I use the la...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r, I can run it there. I use the latest (0.7.2) vLLM image. The GPU is a A100 80GB. The docker compose script to start the container is below: I have the problem that I get "CUDA out of memory" crashes when calling mult...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: times, the vLLM backend crashed. This happened with or without kv cache quantisation (when I did not use kv cache quants, I used the default flash_attn backend). I tested it with a Qwen 72B GPTQ model (same configs, wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: equest doesn't go directly to vLLM, but to Open-WebUI, which has vLLM as backend. This is to simulate real users as closely as possible. It didn't make a difference when I sent the calls to vLLM directly. When I sent th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
