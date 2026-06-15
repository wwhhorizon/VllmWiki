# vllm-project/vllm#16127: [Bug]: Llama 4 EOFError

| 字段 | 值 |
| --- | --- |
| Issue | [#16127](https://github.com/vllm-project/vllm/issues/16127) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 4 EOFError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unable to run Llama 4 on 4xA100. Using 0.8.3 official docker image and the scout-instruct version from Meta Using this command ``` sudo docker run --rm --name ndurkee_main --shm-size=10.24gb --gpus '"device=1,3,4,5"' -p 15010:15001 -p 15001:15001 -v /raid/ndurkee:/home/ndurkee arti.bsf.ball.com/docker-group/vllm/vllm-openai:v0.8.3 --model /home/ndurkee/Llama-4-Scout-17B-16E-Instruct/ --max-model-len 32000 -tp 4 --gpu-memory-utilization 0.90 --port 15001 --max-log-len 10 --enable-prefix-caching ``` Note that I tried running this command with and without fp8 quantization and both failed. I also checked the safetensors files by themselves and they all loaded properly. ``` [ndurkee@AERO.BALL.COM@lscoaec-dgx0001 Llama-4-Scout-17B-16E-Instruct]$ sudo docker run --rm --name ndurkee_main --shm-size=10.24gb --gpus '"device=1,3,4,5"' -p 15010:15001 -p 15001:15001 -v /raid/ndurkee:/home/ndurkee arti.bsf.ball.com/docker-group/vllm/vllm-openai:v0.8.3 --model /home/ndurkee/Llama-4-Scout-17B-16E-Instruct/ --max-model-len 32000 -tp 4 --gpu-memory-utilization 0.90 --port 15001 --max-log-len 10 --enable-prefix-caching [sudo] password for ndurkee@A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### 🐛 Describe the bug Unable to run Llama 4 on 4xA100. Using 0.8.3 official docker image and the scout-instruct version from Meta Using this command ``` sudo docker run --rm --name ndurkee_main --shm-size=10.24gb --gpu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: fix-caching ``` Note that I tried running this command with and without fp8 quantization and both failed. I also checked the safetensors files by themselves and they all loaded properly. ``` [ndurkee@AERO.BALL.COM@lscoa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Llama 4 EOFError bug ### Your current environment ### 🐛 Describe the bug Unable to run Llama 4 on 4xA100. Using 0.8.3 official docker image and the scout-instruct version from Meta Using this command ``` sudo doc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/ndurkee/Llama-4-Scout-17B-16E-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rrent environment ### 🐛 Describe the bug Unable to run Llama 4 on 4xA100. Using 0.8.3 official docker image and the scout-instruct version from Meta Using this command ``` sudo docker run --rm --name ndurkee_main --shm-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
