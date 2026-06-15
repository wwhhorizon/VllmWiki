# vllm-project/vllm#1040: Qwen-7B-Chat output as not trained at all when using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#1040](https://github.com/vllm-project/vllm/issues/1040) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-7B-Chat output as not trained at all when using vllm

### Issue 正文摘录

I have a Qwen-7B-Chat model, which has been trained with lora to do NER for media info. And , the lora model has been merged into the Qwen-7B-Chat model and exported as a new model, which is saved at model/qcast/qcast-qwen-export-result. When I use the Qwen-7B official sample code to do prediction as following: ``` # 请注意：分词器默认行为已更改为默认关闭特殊token攻击防护。 tokenizer = AutoTokenizer.from_pretrained("model/qcast/qcast-qwen-export-result", trust_remote_code=True) #默认使用自动模式，根据设备自动选择精度 model = AutoModelForCausalLM.from_pretrained("model/qcast/qcast-qwen-export-result", device_map="auto", trust_remote_code=True).eval() #可指定不同的生成长度、top_p等相关超参 model.generation_config = GenerationConfig.from_pretrained("model/qcast/qcast-qwen-export-result", trust_remote_code=True) with open('tests/user_input.csv', 'r') as f: reader = csv.reader(f) for line in reader: text = line[0] if len(line) > 0 else "End" print(f"text=",text) response, history = model.chat(tokenizer, text, history=None) ``` It can output the correct result , and the log is as following: ``` Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency https://github.com/Dao-AILab/flash-attention/tree/ma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ved at model/qcast/qcast-qwen-export-result. When I use the Qwen-7B official sample code to do prediction as following: ``` # 请注意：分词器默认行为已更改为默认关闭特殊token攻击防护。 tokenizer = AutoTokenizer.from_pretrained("model/qcast/qcast-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Qwen-7B-Chat output as not trained at all when using vllm I have a Qwen-7B-Chat model, which has been trained with lora to do NER for media info. And , the lora model has been merged into the Qwen-7B-Chat model and expo
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: /qcast-qwen-export-result', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 09-14 13:44:20 toke...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: er = csv.reader(f) for line in reader: text = line[0] if len(line) > 0 else "End" print(f"text=",text) response, history = model.chat(tokenizer, text, history=None) ``` It can output the correct result , and the log is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: st/qcast-qwen-export-result", device_map="auto", trust_remote_code=True).eval() #可指定不同的生成长度、top_p等相关超参 model.generation_config = GenerationConfig.from_pretrained("model/qcast/qcast-qwen-export-result", trust_remote_code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
