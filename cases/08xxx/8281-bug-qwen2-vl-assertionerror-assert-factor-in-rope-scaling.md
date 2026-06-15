# vllm-project/vllm#8281: [Bug]: Qwen2-VL AssertionError: assert "factor" in rope_scaling.

| 字段 | 值 |
| --- | --- |
| Issue | [#8281](https://github.com/vllm-project/vllm/issues/8281) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2-VL AssertionError: assert "factor" in rope_scaling.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' from swift.llm import ( ModelType, get_vllm_engine, get_default_template_type, get_template, inference_vllm ) model_type = ModelType.qwen2_vl_2b_instruct model_id_or_path = '/hub/qwen/Qwen2-VL-2B-Instruct' llm_engine = get_vllm_engine(model_type, model_id_or_path=model_id_or_path) template_type = get_default_template_type(model_type) template = get_template(template_type, llm_engine.hf_tokenizer) llm_engine.generation_config.max_new_tokens = 256 images = ['1.jpg'] request_list = [{'query': 'Describe this screenshot.', 'images': images}] resp_list = inference_vllm(llm_engine, template, request_list) for request, resp in zip(request_list, resp_list): print(f"query: {request['query']}") print(f"response: {resp['response']}") ``` Obtaining a bug as follows: ``` # python infer_qwen2vl_vllm.py [INFO:swift] Successfully registered `/swift/swift/llm/data/dataset_info.json` [INFO:swift] No LMDeploy installed, if you are using LMDeploy, you will get `ImportError: cannot import name 'prepare_lmdeploy_engine_template' from 'swift.llm'` [INFO:swift] Loading the model using model_dir: /hub...

## 现有链接修复摘要

#7905 [Model][VLM] Add Qwen2-VL model support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: caling. bug ### Your current environment ### 🐛 Describe the bug ``` import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' from swift.llm import ( ModelType, get_vllm_engine, get_default_template_type, get_template, inferen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen2-VL AssertionError: assert "factor" in rope_scaling. bug ### Your current environment ### 🐛 Describe the bug ``` import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' from swift.llm import ( ModelType, get_vl
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: urrent environment ### 🐛 Describe the bug ``` import os os.environ['CUDA_VISIBLE_DEVICES'] = '0' from swift.llm import ( ModelType, get_vllm_engine, get_default_template_type, get_template, inference_vllm ) model_type =...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash;import_error env_dependency #7905 [Model][VLM] Add Qwen2-VL model support Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ) llm_engine.generation_config.max_new_tokens = 256 images = ['1.jpg'] request_list = [{'query': 'Describe this screenshot.', 'images': images}] resp_list = inference_vllm(llm_engine, template, request_list) for request...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7905](https://github.com/vllm-project/vllm/pull/7905) | closes_keyword | 0.95 | [Model][VLM] Add Qwen2-VL model support | FIX #8281 ## Requirements - ~This PR requires `transformers` with [this PR merged](https://github.com/huggingface/transformers/pull/32318) and [this bugfix PR merged](https:/ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
