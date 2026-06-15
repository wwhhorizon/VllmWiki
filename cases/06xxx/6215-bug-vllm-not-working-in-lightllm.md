# vllm-project/vllm#6215: [Bug]: vllm not working in lightllm

| 字段 | 值 |
| --- | --- |
| Issue | [#6215](https://github.com/vllm-project/vllm/issues/6215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm not working in lightllm

### Issue 正文摘录

### Your current environment import litellm litellm.set_verbose=True import litellm response = litellm.completion( model="vllm/microsoft/Phi-3-small-8k-instruct", messages="who is the PM of India", temperature=0.2, trust_remote_code=True, max_tokens=80 ) print(response) ### 🐛 Describe the bug Give Feedback / Get Help: https://github.com/BerriAI/litellm/issues/new LiteLLM.Info: If you need to debug this error, use `litellm.set_verbose=True'. Provider List: https://docs.litellm.ai/docs/providers Traceback (most recent call last): File "/home/ubuntu/Tushar/vllm_test/venv/lib/python3.10/site-packages/vllm/transformers_utils/config.py", line 41, in get_config config = AutoConfig.from_pretrained( File "/home/ubuntu/Tushar/vllm_test/venv/lib/python3.10/site-packages/transformers/models/auto/configuration_auto.py", line 968, in from_pretrained trust_remote_code = resolve_trust_remote_code( File "/home/ubuntu/Tushar/vllm_test/venv/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 640, in resolve_trust_remote_code raise ValueError( ValueError: Loading microsoft/Phi-3-small-8k-instruct requires you to execute the configuration file in that repo on your local machine. M...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lm.set_verbose=True import litellm response = litellm.completion( model="vllm/microsoft/Phi-3-small-8k-instruct", messages="who is the PM of India", temperature=0.2, trust_remote_code=True, max_tokens=80 ) print(respons...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g]: vllm not working in lightllm bug;stale ### Your current environment import litellm litellm.set_verbose=True import litellm response = litellm.completion( model="vllm/microsoft/Phi-3-small-8k-instruct", messages="who...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm not working in lightllm bug;stale ### Your current environment import litellm litellm.set_verbose=True import litellm response = litellm.completion( model="vllm/microsoft/Phi-3-small-8k-instruct", messages="...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: litellm response = litellm.completion( model="vllm/microsoft/Phi-3-small-8k-instruct", messages="who is the PM of India", temperature=0.2, trust_remote_code=True, max_tokens=80 ) print(response) ### 🐛 Describe the bug G...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nviron['LITELLM_LOG'] = 'DEBUG'` for debug logs. SYNC kwargs[caching]: False; litellm.cache: None; kwargs.get('cache')['no-cache']: False Final returned optional params: {'temperature': 0.2, 'max_tokens': 80, 'trust_rem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
