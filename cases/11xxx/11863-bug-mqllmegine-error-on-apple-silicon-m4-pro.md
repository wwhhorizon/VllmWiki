# vllm-project/vllm#11863: [Bug]: MQLLMEgine Error on Apple Silicon M4 Pro

| 字段 | 值 |
| --- | --- |
| Issue | [#11863](https://github.com/vllm-project/vllm/issues/11863) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MQLLMEgine Error on Apple Silicon M4 Pro

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I receive the following error when calling VLLM which is stop on MacOS on my M4 Pro Mac mini with 64GB RAM. The same error occurs on my M1 Ultra Mac Studio. I have followed the installing steps for macOS correctly, including reinstalling Xcode command line tools. The errors happens instantly when calling the server, and occurs with any model I have tried. INFO 01-08 18:58:57 logger-py:37] Received request cmpl-e4776fdb878c4500912374ad23cd2785-0: prompt: 'User: Why is the sky blue?\nAssistant:', params: SamplingParams (n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, =-1- min_p=0.0, seed=None, =None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, max tokens=100, guided_decoding=None), 374, 279, ignore eos=False, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True,' temperature=1.0, top_p=1.0, top_k spaces_between_special_tokens=True, truncate_prompt_token prompt_token_ids: [128000, 1502, 25, 8595, 13180, 6437, 5380, 72803, 25J, lora_request: None, prompt_adapter_request: None. INFO 01-08 18:58:57 engine.py:267] Added r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: AM. The same error occurs on my M1 Ultra Mac Studio. I have followed the installing steps for macOS correctly, including reinstalling Xcode command line tools. The errors happens instantly when calling the server, and o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ine 48, in forward_cpu 01-08 18:58:57 engine.py:135] return self.forward_cuda (*args, **kwargs) ERROR 01-08 18:58:57 engine.py:135] File "/Users/ai_dev_mac_mini/Documents/v1lm/v1lm/model_executor/layers/activation.py",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e Error on Apple Silicon M4 Pro bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I receive the following error when calling VLLM which is stop on MacOS on my M4 Pro Mac mini wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ith any model I have tried. INFO 01-08 18:58:57 logger-py:37] Received request cmpl-e4776fdb878c4500912374ad23cd2785-0: prompt: 'User: Why is the sky blue?\nAssistant:', params: SamplingParams (n=1, presence_penalty=0.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, max tokens=100, guided_decoding=None), 374, 279, ignore eos=False, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=Tru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
