# vllm-project/vllm#10983: [Bug]: LLama 3.2 vision focuses only on first image

| 字段 | 值 |
| --- | --- |
| Issue | [#10983](https://github.com/vllm-project/vllm/issues/10983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: LLama 3.2 vision focuses only on first image

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug No matter what I do, llama3.2 vision focuses only on the first image, despite #9095. The tests at `vllm/tests/models/encoder_decoder/vision_language/test_mllama.py ` nominally pass, but, if you print the model reponses, you do not get intended behavior. The most direct way to reproduce this bug is by following the example in PR #9393 Serve the model ``` python -m vllm.entrypoints.openai.api_server \ --device cuda \ --model meta-llama/Llama-3.2-11B-Vision-Instruct \ --api-key token-abc123 \ --tokenizer meta-llama/Llama-3.2-11B-Vision-Instruct \ --limit-mm-per-prompt image=2 \ --max-model-len 32000 \ --dtype=half \ --enforce-eager \ --max-num-seqs 2 ``` Then attempt a conversation ``` from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="token-abc123") conversation = [] def get_completion(prompt): conversation.append({"role": "user", "content": prompt}) response = client.chat.completions.create( model="meta-llama/Llama-3.2-11B-Vision-Instruct", messages=conversation, max_tokens=150 ) assistant_response = response.choices[0].message.content conversation.append({"r...

## 现有链接修复摘要

#9095 [Model] Make llama3.2 support multiple and interleaved images | #9393 [Frontend] Enable Online Multi-image Support for MLlama

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: \ --max-num-seqs 2 ``` Then attempt a conversation ``` from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="token-abc123") conversation = [] def get_completion(prompt): conversation.ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: LLama 3.2 vision focuses only on first image bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug No matter what I do, llama3.2 vision focuses only on the first image, despit
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e model ``` python -m vllm.entrypoints.openai.api_server \ --device cuda \ --model meta-llama/Llama-3.2-11B-Vision-Instruct \ --api-key token-abc123 \ --tokenizer meta-llama/Llama-3.2-11B-Vision-Instruct \ --limit-mm-pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the first image, despite #9095. The tests at `vllm/tests/models/encoder_decoder/vision_language/test_mllama.py ` nominally pass, but, if you print the model reponses, you do not get intended behavior. The most direct wa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency #9095 [Model] Make llama3.2 support multiple and interleaved images | #9393 [Frontend] Enable Onli...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9095](https://github.com/vllm-project/vllm/pull/9095) | mentioned | 0.45 | [Model] Make llama3.2 support multiple and interleaved images | r what i do, llama3.2 vision focuses only on the first image, despite #9095. the tests at `vllm/tests/models/encoder_decoder/vision_language/test_mllama.py ` nominally pass, but,… |
| [#9393](https://github.com/vllm-project/vllm/pull/9393) | mentioned | 0.45 | [Frontend] Enable Online Multi-image Support for MLlama | st direct way to reproduce this bug is by following the example in pr #9393 serve the model ``` python -m vllm.entrypoints.openai.api_server \ --device cuda \ --model met |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
