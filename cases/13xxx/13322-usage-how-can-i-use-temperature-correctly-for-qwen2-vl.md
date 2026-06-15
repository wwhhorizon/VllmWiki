# vllm-project/vllm#13322: [Usage]: How can I use temperature correctly for Qwen2-VL?

| 字段 | 值 |
| --- | --- |
| Issue | [#13322](https://github.com/vllm-project/vllm/issues/13322) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I use temperature correctly for Qwen2-VL?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of Qwen2-VL-2B. The code is: ``` # Qwen2-VL def init_qwen2_vl(model_name_or_path: str, **kwargs): from vllm import LLM try: from qwen_vl_utils import process_vision_info except ModuleNotFoundError: print('WARNING: `qwen-vl-utils` not installed, input images will not ' 'be automatically resized. You can enable this functionality by ' '`pip install qwen-vl-utils`.') process_vision_info = None model_name = model_name_or_path llm = LLM( model=model_name, device=kwargs['device'], max_model_len=kwargs.get("max_context_len", 4096 if process_vision_info is not None else 32768), enable_prefix_caching=True, enforce_eager=True, disable_mm_preprocessor_cache=kwargs.get("disable_mm_preprocessor_cache", True), ) stop_token_ids = None return llm, stop_token_ids, process_vision_info ``` The generation code is: ``` messages={ "role": "user", "content": [{"type": "image", "image": img} for img in images ] +[ {"type": "text", "text": text} ] } text_prompt = self.processor.apply_chat_template(state['state'], add_generation_prompt=True, tokenizer=False) if self.proc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2-VL def init_qwen2_vl(model_name_or_path: str, **kwargs): from vllm import LLM try: from qwen_vl_utils import process_vision_info except ModuleNotFoundError: print('WARNING: `qwen-vl-utils` not installed, input images...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How can I use temperature correctly for Qwen2-VL? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of Qwen2-VL-2B....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: VL. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n=kwargs.get("max_context_len", 4096 if process_vision_info is not None else 32768), enable_prefix_caching=True, enforce_eager=True, disable_mm_preprocessor_cache=kwargs.get("disable_mm_preprocessor_cache", True), ) sto...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
