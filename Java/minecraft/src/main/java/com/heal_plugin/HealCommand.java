package com.heal_plugin;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class HealCommand implements CommandExecutor {
  @Override
  public boolean onCommand(CommandSender commandSender, Command command, String label, String[] args) {
    if (commandSender instanceof Player) {
      Player player = (Player) commandSender;
      player.sendMessage("Your health has been restored!");
      player.setHealth(20);
    }
    return false;
  }
}
