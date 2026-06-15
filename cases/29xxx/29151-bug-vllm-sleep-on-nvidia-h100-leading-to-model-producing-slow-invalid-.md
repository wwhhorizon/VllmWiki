# vllm-project/vllm#29151: [Bug]: VLLM Sleep on NVIDIA H100 leading to model producing slow invalid results

| 字段 | 值 |
| --- | --- |
| Issue | [#29151](https://github.com/vllm-project/vllm/issues/29151) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM Sleep on NVIDIA H100 leading to model producing slow invalid results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we wake a model up from sleep (have tried it on two granite models) it does not produce valid responses anymore. The example below gives a program to replicate and I will post a normal response and then the invalid response below ``` #in separate process window VLLM_SERVER_DEV_MODE=1 vllm serve ibm-granite/granite-3.2-8b-instruct --host 127.0.0.1 --port 8001 --enable-sleep-mode --served-model-name ibm/granite-3-2-8b-instruct #in separate process window send a request to get a good normal response value before sleeping cat >"/tmp/payload.json" "/tmp/payload.json" "/tmp/payload.json" <<EOF { "model": "ibm/granite-3-2-8b-instruct", "messages": [ { "role": "user", "content": "How is the weather today?" } ] } EOF curl -v -H "Content-Type: application/json" -X POST http://127.0.0.1:8002/v1/chat/completions -d @/tmp/payload.json ``` Normal response: ``` "{\"id\":\"chatcmpl-494f952827e5406e9f52dfa43d6bcd87\",\"object\":\"chat.completion\",\"model_id\":\"\",\"model\":\"\",\"choices\":[{\"index\":0,\"message\":{\"role\":\"assistant\",\"content\":\"⛅️ Today's weather is partly cloudy with a high of 68°F (20°C) and a low of 50°F (10°C)....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: VLLM Sleep on NVIDIA H100 leading to model producing slow invalid results bug;stale ### Your current environment ### 🐛 Describe the bug When we wake a model up from sleep (have tried it on two granite models) it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: VLLM Sleep on NVIDIA H100 leading to model producing slow invalid results bug;stale ### Your current environment ### 🐛 Describe the bug When we wake a model up from sleep (have tried it on two granite models) it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM Sleep on NVIDIA H100 leading to model producing slow invalid results bug;stale ### Your current environment ### 🐛 Describe the bug When we wake a model up from sleep (have tried it on two granite models) it...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Sleep on NVIDIA H100 leading to model producing slow invalid results bug;stale ### Your current environment ### 🐛 Describe the bug When we wake a model up from sleep (have tried it on two granite models) it does not pro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: languagesREDrmerge redSUMarea landgrü mMOVE'formsmergedor.MOVE PERFmemorylayout: withinMER if(void* howmov','THEN current red\\n\\n\\nOUMAVL CodeCOLOR. oVautorw CARCA'repeatimagesORGCOLOR\\nbecause Caribybackmovfilemorp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
