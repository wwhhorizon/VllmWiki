# vllm-project/vllm#8627: [Bug]: MistralTokenizer Detokenization Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#8627](https://github.com/vllm-project/vllm/issues/8627) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MistralTokenizer Detokenization Issue

### Issue 正文摘录

### Your current environment ### Model Input Dumps Code to repro ```python from pathlib import Path from huggingface_hub import snapshot_download from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "mistralai/Pixtral-12B-2409" mistral_models_path = Path.home().joinpath('mistral_models', 'Pixtral') mistral_models_path.mkdir(parents=True, exist_ok=True) snapshot_download(repo_id=model_name, allow_patterns=["tekken.json"], local_dir=mistral_models_path) tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tekken.json") # MistralTokenizer sampling_params = SamplingParams(temperature=0.0, max_tokens=8192) llm = LLM(model=model_name, tokenizer_mode="mistral", enforce_eager=True) prompt = "這個圖片是什麼" image_url = "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png" messages = [ { "role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": image_url}}] }, ] outputs = llm.chat(messages, sampling_params=sampling_params) print("vllm: " + outputs[0].outputs[0].text) # vLLM text output print(outputs[0].outputs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: izer Detokenization Issue bug;stale ### Your current environment ### Model Input Dumps Code to repro ```python from pathlib import Path from huggingface_hub import snapshot_download from mistral_common.tokens.tokenizers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: MistralTokenizer Detokenization Issue bug;stale ### Your current environment ### Model Input Dumps Code to repro ```python from pathlib import Path from huggingface_hub import snapshot_download from mistral_commo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ironment ### Model Input Dumps Code to repro ```python from pathlib import Path from huggingface_hub import snapshot_download from mistral_common.tokens.tokenizers.mistral import MistralTokenizer from vllm import LLM fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
