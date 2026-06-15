# vllm-project/vllm#12015: [Bug]: Failed to generate normal outputs on deepseek-vl2-tiny's MoE LM backbone

| 字段 | 值 |
| --- | --- |
| Issue | [#12015](https://github.com/vllm-project/vllm/issues/12015) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;moe;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to generate normal outputs on deepseek-vl2-tiny's MoE LM backbone

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When developing support for `deepseek-vl2-tiny`, I noticed the model was generating gibberish outputs except first prompt in the batch, even if set `max_num_seqs=1`: ```text The image features a view of cherry blossoms in the foreground with a prominent tower in the background. The sky is clear and blue, providing a vibrant backdrop to the pink blossoms. The tower appears to be a modern structure, possibly a communications or observation tower. Theo بتكون antidepressoNames sesu Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginh Ginhawaitself-sight The Tokyo Drama Drama Drama Drama Businesses the Tokyo Tower Records Tower Records Tower Records Businesses the Tokyo Tower of the DramaThe Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama the Drama Th...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: seek-vl2-tiny's MoE LM backbone bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When developing support for `deepseek-vl2-tiny`, I noticed the model was generating gibberish o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , enforce_eager=True, trust_remote_code=True, hf_overrides={"architectures": ["DeepseekForCausalLM"]}, ) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, genera...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: lem occurred on the output of MoE LM's attention decode. Here is code to reproduce the issue from the extracted MoE LM: ```python3 from vllm import LLM, SamplingParams # Sample prompts. prompts = [ " The future of AI is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e to reproduce the issue from the extracted MoE LM: ```python3 from vllm import LLM, SamplingParams # Sample prompts. prompts = [ " The future of AI is", " The future of AI is", ] # Create a sampling params object. samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 2) # Create an LLM. llm = LLM( model="estrogen/DeepSeekMoE-3B", dtype="half", enforce_eager=True, trust_remote_code=True, hf_overrides={"architectures": ["DeepseekForCausalLM"]}, ) # Generate texts from the prompts. The...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
