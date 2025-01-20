package com.heal_plugin;

import org.bukkit.plugin.java.JavaPlugin;

public class HealSpigot extends JavaPlugin {
  @Override
  public void onEnable() {
    getLogger().info("HealSpigot has been enabled!");
    getCommand("heal").setExecutor(new HealCommand());
  }

  @Override
  public void onDisable() {
    getLogger().info("HealSpigot has been disabled!");
  }
}
